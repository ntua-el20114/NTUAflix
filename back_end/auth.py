from flask import request, jsonify, make_response, session
from functools import wraps
from flask_restful import Resource
import json, jwt, datetime
from back_end import app
from flask_cors import cross_origin
import random
import os

from back_end import db

def login_user(username, password):
    # Check if the user exists and the password is correct
    cur = db.get_db().cursor()
    cur.execute("SELECT * FROM app_user WHERE username=%s AND password=%s", (username, password))
    user = cur.fetchone()
    print(user)
    cur.close()

    if user:
        # Set expiration time to 24 hours
        expiration_time = datetime.datetime.utcnow() + datetime.timedelta(days=1)
        # Create payload
        payload = {
            'exp': expiration_time,
            'iat': datetime.datetime.utcnow(),
            'jti': os.urandom(16).hex(),
            'sub': user["id"]
        }
        # Now 'token' contains the JWT that can be sent to the client

        #Update the user's token into the database with the newly encoded one
        token = jwt.encode(payload, app.config["SECRET_KEY"], algorithm="HS256")
        cur = db.get_db().cursor()
        cur.execute("UPDATE app_user SET token=%s WHERE id=%s", [token, user["id"]])
        db.get_db().commit()
        cur.close()
        return token

        """
        # Get the user's token from the database
        token=user["token"]
        return token
        """
    return None

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # Check if the token is present in the headers
        token = None
        if "X-OBSERVATORY-AUTH" in request.headers:
            token = request.headers.get('X-OBSERVATORY-AUTH')
        if not token:
            return make_response(jsonify({'Error': 'Token not in headers, please login first'}), 401)
        try:
            token_decoded = jwt.decode(token, app.config["SECRET_KEY"], algorithms=["HS256"])
        except jwt.ExpiredSignatureError:
            return make_response(jsonify({'Error': 'Token expired.'}), 401)
        user_id_from_token = token_decoded.get('sub')  # Extract user ID from decoded token
        try:
            cur = db.get_db().cursor()
            cur.execute("SELECT * FROM app_user WHERE id = %s", [user_id_from_token])
            current_user = cur.fetchone()
            cur.close()
            if current_user is None:
                return make_response(jsonify({'Error': 'User not found'}), 401)
            kwargs['user'] = current_user
            return f(*args, **kwargs)
        except Exception as e:
            return make_response(jsonify({'Error': str(e)}), 500)
        """
        if "token" not in session:
            return make_response(jsonify({'Error': 'Token not in session, please login first'}), 401)
        token = session["token"]
        if not token:
            return make_response(jsonify({'Error': 'Token not found, please login first'}), 401)

        # Check if the token is valid
        cur = db.get_db().cursor()
        cur.execute("SELECT * FROM app_user where token=%s",[token])
        user = cur.fetchone()
        cur.close()

        if not user:
            return make_response(jsonify({'Error': 'User not found'}), 401)

        # Add the user object to the kwargs for the route function to access
        kwargs['user'] = user
        return f(*args, **kwargs)
        """
    return decorated_function

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # Check if the user is an admin
        current_user = kwargs['user']
        try:
            if current_user and current_user["user_role"] == "administrator":
                return f(*args, **kwargs)
            else:
                response = make_response(jsonify({'Error': 'Unauthorized. Only admin can access this resource'}), 401)
                response.headers.add('X-OBSERVATORY-AUTH', current_user["token"])  # Assuming the token is stored in the user object
                return response
        except Exception as e:
            return make_response(jsonify({'Error': str(e)}), 500)  
    return decorated_function

def getTitleObject(titleID):
    cur = db.get_db().cursor()
    cur.execute("SELECT title_id as titleID, titleType as type, originalTitle, url as titlePoster, startYear, genres FROM title WHERE title_id = %s", (titleID,))
    result = cur.fetchone()
    cur.execute("SELECT title as akaTitle, region as regionAbbrev FROM aka WHERE title_id = %s", (titleID,))
    result_2_tuple = cur.fetchall()
    cur.execute("""
            SELECT p.name_id as nameID, n.primaryName as name, p.category as category 
            FROM principals p
            INNER JOIN name n
            ON n.name_id = p.name_id 
            WHERE p.title_id = %s""", (titleID,))
    result_3_tuple = cur.fetchall()
    cur.execute("""
            SELECT averageRating as avRating, numVotes as nVotes
            FROM imdb_rating
            WHERE title_id = %s""", (titleID,))
    result_4_tuple = cur.fetchall()
    cur.close()

    #proccess the data to be as needed
    if not result:
        return {"error": "No title with this titleID."}
    genres_str = result.get("genres")
    genres_list = [genre.strip("'") for genre in genres_str.split(",")] if genres_str else []

    result_2 = [dict(row) for row in result_2_tuple]
    result_3 = [dict(row) for row in result_3_tuple]
    result_4 = [dict(row) for row in result_4_tuple]

    keys = ['titleID', 'type', 'originalTitle', 'titlePoster', 'startYear', 'endYear']
    
    
    return_dict = {}
    for i in range(0, 6):
        key = keys[i]
        curr = result.get(key)
        # Check NULL value
        if curr is None:
            curr = "Null"
        return_dict[key] = curr
    return_dict["genres"] = genres_list
    return_dict["titleAkas"] = "None" if len(result_2)==0 else result_2
    return_dict["principals"] = "None" if len(result_3)==0 else result_3
    return_dict["rating"] = "None" if len(result_4)==0 else result_4
    return return_dict

def getNameObject(nameID):
    cur = db.get_db().cursor()
    cur.execute(""" 
                SELECT name_id as nameID, primaryName as name, url as namePoster ,birthYear as birthYr, deathYear as deathYr, primaryProfession as profession
                FROM name
                WHERE name_id = %s""", (nameID,))    
    result = cur.fetchone()
    cur.execute(""" 
                SELECT p.title_id, p.category
                FROM principals p
                INNER JOIN name n
                ON p.name_id = n.name_id
                WHERE n.name_id = %s""", (nameID,))
    result_2_tuple = cur.fetchall()
    cur.close()
    if not result:
        return {"error": "No name with this nameID."}
    
    result_2 = [dict(row) for row in result_2_tuple]

    return_dict = {}
    keys = ['nameID', 'name', 'namePoster','birthYr', 'deathYr', 'profession']
    
    for i in range(0, 6):
        # Take the i-th result from the query
        key = keys[i]
        curr = result.get(key)
        # Check NULL value
        if curr == None:
            curr = "Null"
        return_dict[key] = curr

    return_dict["nameTitles"] = "None" if len(result_2)==0 else result_2
    return return_dict

class UserRole(Resource):
    @cross_origin()
    @login_required
    def get(self, user):  
        response_data = {'user_role': user["user_role"]}
        response = make_response(jsonify(response_data), 200)
        response.headers.add('X-OBSERVATORY-AUTH',user["token"])
        return response

class UserLogin(Resource):
    def post(self):
        username = request.form.get('username')
        password = request.form.get('password')
        if not username or not password:
            return {'error': 'Missing username or password in the request body'}, 400

        #check if user exists
        cur = db.get_db().cursor()
        cur.execute("SELECT username FROM app_user where username=%s",[username])
        get_user = cur.fetchall()
        cur.close()

        if  not get_user:
            return {'error': f'User {username} does not exist'}, 400
        cur = db.get_db().cursor()
        cur.execute("SELECT user_role FROM app_user where username=%s",[username])
        get_user = cur.fetchall()
        cur.close()
        if not get_user:
            return {'error': f'User {username} does not exist'}, 400

        user_role = get_user[0]["user_role"]

        token = login_user(username, password)

        response_data = {'token': token, 'user_role': user_role}
        response = make_response(jsonify(response_data), 200)
        response.headers.add('X-OBSERVATORY-AUTH', token)
        return response
    def get(self):
        return {"message": "You should make a POST request to login"}, 400

class UserLogout(Resource):
    @cross_origin()
    @login_required
    def post(self, user):
        if 'X-OBSERVATORY-AUTH' in request.headers:
            response = make_response('', 200)
            return response
        else:
            # The token is not present in the headers, which means the user is already considered logged out
            return {'message': 'User is already logged out'}, 200

class GetTitle(Resource):
    @cross_origin()
    @login_required
    def get(self, user, titleID):
        return_dict = getTitleObject(titleID)
        json_result = json.dumps(return_dict, sort_keys=False)
        if "error" in return_dict:
            return make_response(json_result, 400)
        response = make_response(json_result, 200)
        response.headers.add('X-OBSERVATORY-AUTH', user["token"])
        return response

class SearchTitle(Resource):
    @cross_origin()
    @login_required
    def get(self, user):
        data = request.form.get("titlePart")
        if not data:
            return {'error': 'Missing titlePart in the request body'}, 400
        part_of_title = data

        # Execute the query to search for titles
        cur = db.get_db().cursor()
        cur.execute(f"SELECT title_id FROM title WHERE originalTitle LIKE '%{part_of_title}%'")
        result = cur.fetchall()
        cur.close()
        if not result:
            response = make_response(jsonify({"message": "No originalTitle found containing this titlePart."}), 204)
            response.headers.add('X-OBSERVATORY-AUTH', user.get("token"))  # Assuming the token is stored in the user object
            return response
        return_list = [getTitleObject(title_id['title_id']) for title_id in result]
        return_dict = {}
        return_dict["result"] = return_list

        json_result = json.dumps(return_dict, sort_keys=False)
        response = make_response(json_result, 200)
        #response.headers.add('X-OBSERVATORY-AUTH', user.get("token"))  # Assuming the token is stored in the user object
        return response

class ByGenre(Resource):
    @cross_origin()
    @login_required
    def get(self, user):
        genre = request.form.get('qgenre')
        minrating = request.form.get('minrating')
        yrFrom = request.form.get('yrFrom')
        yrTo = request.form.get('yrTo')

        if not genre:
            return {"error": "qgenre not found in request body"}, 400
        if not minrating:
            return {"error": "minrating not found in request body"}, 400

        #get list of possible genres
        cur = db.get_db().cursor()
        cur.execute("SHOW COLUMNS FROM title LIKE 'genres'")
        genres_table = cur.fetchone()
        genres_str = genres_table["Type"]
        #genres = [g.strip("'") for g in genres_str[5:-1].split(", ")]        
        genres = ['Action','Adult','Adventure','Animation','Biography','Comedy','Crime','Documentary',
                 'Drama','Family','Fantasy','History','Horror','Music','Musical','Mystery','News',
                 'Romance','Sci-Fi','Short','Sport','Thriller','War','Western']

        if genre not in genres:
            return {"error": "Provide a valid genre."}, 400

        query = """
            SELECT DISTINCT t.*
            FROM title t
            JOIN imdb_rating ir ON t.title_id = ir.title_id
            JOIN principals p ON t.title_id = p.title_id
            WHERE FIND_IN_SET(%s, t.genres) > 0
            AND ir.averageRating >= %s
        """
        params = (genre, minrating)
        if yrFrom:
            query += " AND t.startYear >= %s"
            params += (yrFrom,)
        if yrTo:
            query += " AND t.startYear <= %s"
            params += (yrTo,)

        cur.execute(query, params)
        titles = cur.fetchall()
        cur.close()

        # Prepare the response
        response_data = [{'title_id': title['title_id'],
                          'titleType': title['titleType'],
                          'originalTitle': title['originalTitle'],
                          'startYear': title['startYear'],
                          'genres': title['genres']}
                         for title in titles]

        return_dict = {}
        return_dict["result"] = response_data

        json_result = json.dumps(return_dict, sort_keys=False)
        response = make_response(json_result, 200)

        # response = make_response(jsonify(response_data), 200)
        # response.headers.add('X-OBSERVATORY-AUTH', user["token"])  # Assuming the token is stored in the user object
        return response

class GetName(Resource):
    @cross_origin()
    @login_required
    def get(self, user, nameID):
        return_dict = getNameObject(nameID)
        json_result = json.dumps(return_dict, sort_keys=False)
        if "error" in return_dict:
            return make_response(json_result, 400) 
        response = make_response(json_result, 200)
        response.headers.add('X-OBSERVATORY-AUTH', user["token"])  # Assuming the token is stored in the user object
        return response

class SearchName(Resource):
    @cross_origin()
    @login_required
    def get(self, user):
        data = request.form.get("namePart")
        if not data:
            return {'error': 'Missing namePart in the request body'}, 400
        part_of_name = data

        # Execute the query to search for names
        cur = db.get_db().cursor()
        cur.execute(f"SELECT name_id FROM name WHERE primaryName LIKE '%{part_of_name}%'")
        result = cur.fetchall()
        cur.close()
        if not result:
            response = make_response(jsonify({"message": "No primaryName found containing this namePart."}), 204)
            response.headers.add('X-OBSERVATORY-AUTH', user.get("token"))  # Assuming the token is stored in the user object
            return response
        return_list = [getNameObject(name_id['name_id']) for name_id in result]
        return_dict = {}
        return_dict["result"] = return_list
        json_result = json.dumps(return_dict, sort_keys=False)
        response = make_response(json_result, 200)
        response.headers.add('X-OBSERVATORY-AUTH', user["token"])  # Assuming the token is stored in the user object
        return response

############################################# Rating Movies for Web App #########################################
#################################################################################################################

class RateMovie(Resource):
    @cross_origin()
    @login_required
    def post(self,user):
        rating = request.form.get("rating")
        title_id = request.form.get("title_id")
        user_id = user.get("id")

        if not rating:
            return {'error': 'Missing rating in the request body'}, 400

        if not title_id:
            return {'error': 'issing title_id in the request body'}, 400

        # Check if the user has already rated the movie
        cur = db.get_db().cursor()
        cur.execute(f"SELECT * FROM user_rating WHERE user_id = {user_id} and title_id = '{title_id}'")
        result = cur.fetchone()
        cur.close()
        print(result)
        print(rating)
        print(title_id)
        print(user_id)

        # If the user has already rated the movie, update the rating
        if result:
            # If the user unlikes or undislikes
            if rating == '0':
                cur = db.get_db().cursor()
                cur.execute(f"DELETE FROM user_rating WHERE user_id = {user_id} and title_id = '{title_id}';")
                db.get_db().commit()
                cur.close()

                cur = db.get_db().cursor()
                cur.execute(f"DELETE FROM user_preferences WHERE user_id = {user_id} and title_id = '{title_id}';")
                cur = db.get_db().cursor()
                db.get_db().commit()
                cur.close()

                return {"status":"Rating deleted"}, 200

            # If the user likes
            if rating == '1':
                print("In rating = 1 after having already a rating")
                cur = db.get_db().cursor()
                cur.execute(f"INSERT INTO user_preferences (user_id, title_id) VALUES ({user_id}, '{title_id}');")
                db.get_db().commit()
                cur.close()

                cur = db.get_db().cursor()
                cur.execute(f"UPDATE user_rating SET rating = {rating} WHERE user_id = {user_id} and title_id = '{title_id}'")
                db.get_db().commit()
                cur.close()

                return {"status":"Rating added"}, 200

            if rating == '-1':
                print("In rating = -1 after having already a rating")
                cur = db.get_db().cursor()
                cur.execute(f"UPDATE user_rating SET rating = {rating} WHERE user_id = {user_id} and title_id = '{title_id}'")
                db.get_db().commit()
                cur.close()

                cur = db.get_db().cursor()
                cur.execute(f"DELETE FROM user_preferences WHERE user_id = {user_id} and title_id = '{title_id}';")
                db.get_db().commit()
                cur.close()

                return {"status":"Rating added"}, 200


        # If the user hasn't rated yet
        else:
            try:
                cur = db.get_db().cursor()
                cur.execute(f"INSERT INTO user_rating (user_id, title_id, rating) VALUES ({user_id}, '{title_id}', {rating});")
                db.get_db().commit()
                cur.close()

                if rating == '1':
                    cur = db.get_db().cursor()
                    cur.execute(f"INSERT INTO user_preferences (user_id, title_id) VALUES ({user_id}, '{title_id}');")
                    db.get_db().commit()
                    cur.close()

                    return {"status":"Rating added"}, 200

                else:
                    cur = db.get_db().cursor()
                    cur.execute(f"DELETE FROM user_preferences WHERE user_id = {user_id} and title_id = '{title_id}';")
                    db.get_db().commit()
                    cur.close()

                    return {"status":"Rating added"}, 200

            except Exception as e:
                return {'error here': f'{str(e)}'}, 400

        return {"status":"Rating added"}, 200


class GetLikedMovies(Resource):
    @cross_origin()
    @login_required
    def get(self, user):
        user_id = user.get("id")

        query = f"SELECT * FROM user_rating WHERE user_id = {user_id} AND rating = 1;"

        try:
            cur = db.get_db().cursor()
            cur.execute(query)
            result = cur.fetchall()
            cur.close()
            return_list = [getTitleObject(item['title_id']) for item in result]
            return_dict = {}
            return_dict["result"] = return_list

            json_result = json.dumps(return_dict, sort_keys=False)
            response = make_response(json_result, 200)
            return response
        except Exception as e:
            return {'error': f'{str(e)}'}, 400

class GetDislikedMovies(Resource):
    @cross_origin()
    @login_required
    def get(self,user):
        user_id = user.get("id")

        query = f"SELECT * FROM user_rating WHERE user_id = {user_id} AND rating = -1;"

        try:
            cur = db.get_db().cursor()
            cur.execute(query)
            result = cur.fetchall()
            cur.close()
            return_list = [getTitleObject(item['title_id']) for item in result]
            return_dict = {}
            return_dict["result"] = return_list

            json_result = json.dumps(return_dict, sort_keys=False)
            response = make_response(json_result, 200)
            return response
        except Exception as e:
            return {'error': f'{str(e)}'}, 400

class GetTopRatedMovies(Resource):
    @cross_origin()
    @login_required
    def get(self, user):
        query = f"SELECT * FROM imdb_rating ORDER BY averageRating DESC LIMIT 30;"

        try:
            cur = db.get_db().cursor()
            cur.execute(query)
            result = cur.fetchall()
            cur.close()
            return_list = [getTitleObject(item['title_id']) for item in result]
            return_dict = {}
            return_dict["result"] = return_list

            json_result = json.dumps(return_dict, sort_keys=False)
            response = make_response(json_result, 200)
            return response
        except Exception as e:
            return {'error': f'{str(e)}'}, 400

class GetAppUserData(Resource):
    @cross_origin()
    @login_required
    def get(self,user):
        user_id = user.get("id")

        query = f"SELECT * FROM app_user WHERE id = {user_id};"

        try:
            cur = db.get_db().cursor()
            cur.execute(query)
            result = cur.fetchall()
            cur.close()
            if result:
                response_data = {'id': result[0]['id'],
                                  'user_role': result[0]['user_role'],
                                  'token': result[0]['token'],
                                  'first_name': result[0]['first_name'],
                                  'last_name': result[0]['last_name'],
                                  'birthdate': result[0]['birthdate'],
                                  'email': result[0]['email'],
                                  'username': result[0]['username'],
                                  'password': result[0]['password']}
                return_dict = {}
                return_dict["result"] = response_data

                response = make_response(response_data, 200)
                return response
            else:
                return {'error':'no such user'}, 400
        except Exception as e:
            return {'error': f'{str(e)}'}, 400

