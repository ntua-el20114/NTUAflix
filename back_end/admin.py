from flask import Flask, request, make_response
from flask_restful import Resource
import secrets,  json
from back_end import db, app
from .auth import login_required, admin_required

class HealthCheck(Resource):
    @login_required
    @admin_required
    def get(self, user):
        try:
            #check if user exists
            cur = db.get_db().cursor()
            cur.execute("show tables")
            cur.close()

            connection_string = f"mysql://root@localhost/ntuaflix"
            return {"status": "OK", "dataconnection": connection_string}, 200

        except Exception as e:
            return {"status": "failed", "dataconnection": f"Database connection failed. Error: {str(e)}"}, 500
class TitleBasics(Resource):
    @login_required
    @admin_required
    # Read TSV data from the specified file
    def post(self, user):
        tsv_data = request.form.get("tsv_data")
        # Split the TSV data into lines
        lines = tsv_data.strip().split('\n')

        # Extract column headers and data
        column_headers = lines[0].split('\t')
        data_lines = lines[1:]
        # Create the SQL query for inserting data into the specified table
        sql_query = f"INSERT IGNORE INTO title ({', '.join(column_headers)}) VALUES "

        # Append each data line to the SQL query
        for line in data_lines:
            values = line.split('\t')
            formatted_values = [f"'{value}'" if (value and value!='None') else 'NULL' for value in values]
            sql_query += f"({', '.join(formatted_values)}), "

        # Remove the trailing comma and execute the SQL query
        sql_query = sql_query.rstrip(', ')
        cur = db.get_db().cursor()
        cur.execute(sql_query)
        db.get_db().commit()
        cur.close()

        return {"status":"Titles added"}, 200

class TitleAkas(Resource):
    @login_required
    @admin_required
    def post(self, user):
        tsv_data = request.form.get("tsv_data")
            
        # Split the TSV data into lines
        lines = tsv_data.strip().split('\n')

        # Extract column headers and data
        column_headers = lines[0].split('\t')
        data_lines = lines[1:]

        # Create the SQL query for inserting data into the specified table
        sql_query = f"INSERT IGNORE INTO aka ({', '.join(column_headers)}) VALUES "

        # Append each data line to the SQL query
        for line in data_lines:
            values = line.split('\t')
            formatted_values = [f"'{value}'" if (value and value!='None') else 'NULL' for value in values]
            sql_query += f"({', '.join(formatted_values)}), "
        
        # Remove the trailing comma and execute the SQL query
        sql_query = sql_query.rstrip(', ')
        cur = db.get_db().cursor()
        cur.execute(sql_query)
        db.get_db().commit()
        cur.close()

        return {"status":"Akas added"}, 200

class NameBasics(Resource):
    @login_required
    @admin_required
    def post(self, user):
        tsv_data = request.form.get("tsv_data")
            
        # Split the TSV data into lines
        lines = tsv_data.strip().split('\n')

        # Extract column headers and data
        column_headers = lines[0].split('\t')
        data_lines = lines[1:]

        # Create the SQL query for inserting data into the specified table
        sql_query = f"INSERT IGNORE INTO name ({', '.join(column_headers)}) VALUES "

        # Append each data line to the SQL query
        for line in data_lines:
            values = line.split('\t')
            formatted_values = [f"'{value}'" if (value and value!='None') else 'NULL' for value in values]
            sql_query += f"({', '.join(formatted_values)}), "
        
        # Remove the trailing comma and execute the SQL query
        sql_query = sql_query.rstrip(', ')
        cur = db.get_db().cursor()
        cur.execute(sql_query)
        db.get_db().commit()
        cur.close()

        return {"status":"Names added"}, 200

class TitleCrew(Resource):
    @login_required
    @admin_required
    def post(self, user):
        tsv_data = request.form.get("tsv_data")
            
        # Split the TSV data into lines
        lines = tsv_data.strip().split('\n')

        # Extract column headers and data
        column_headers = lines[0].split('\t')
        data_lines = lines[1:]

        # Create the SQL query for inserting data into the specified table
        sql_query = f"INSERT IGNORE INTO crew ({', '.join(column_headers)}) VALUES "

        # Append each data line to the SQL query
        for line in data_lines:
            values = line.split('\t')
            formatted_values = [f"'{value}'" if (value and value!='None') else 'NULL' for value in values]
            sql_query += f"({', '.join(formatted_values)}), "
        
        # Remove the trailing comma and execute the SQL query
        sql_query = sql_query.rstrip(', ')
        cur = db.get_db().cursor()
        cur.execute(sql_query)
        db.get_db().commit()
        cur.close()

        return {"status":"Crews added"}, 200

class TitleEpisode(Resource):
    @login_required
    @admin_required
    def post(self, user):
        tsv_data = request.form.get("tsv_data")
            
        # Split the TSV data into lines
        lines = tsv_data.strip().split('\n')

        # Extract column headers and data
        column_headers = lines[0].split('\t')
        data_lines = lines[1:]

        # Create the SQL query for inserting data into the specified table
        sql_query = f"INSERT IGNORE INTO episodes ({', '.join(column_headers)}) VALUES "

        # Append each data line to the SQL query
        for line in data_lines:
            values = line.split('\t')
            formatted_values = [f"'{value}'" if (value and value!='None') else 'NULL' for value in values]
            sql_query += f"({', '.join(formatted_values)}), "
        
        # Remove the trailing comma and execute the SQL query
        sql_query = sql_query.rstrip(', ')
        cur = db.get_db().cursor()
        cur.execute(sql_query)
        db.get_db().commit()
        cur.close()

        return {"status":"Episodes added"}, 200

class TitlePrincipal(Resource):
    @login_required
    @admin_required
    def post(self, user):
        tsv_data = request.form.get("tsv_data")
            
        # Split the TSV data into lines
        lines = tsv_data.strip().split('\n')

        # Extract column headers and data
        column_headers = lines[0].split('\t')
        data_lines = lines[1:]

        # Create the SQL query for inserting data into the specified table
        sql_query = f"INSERT IGNORE INTO principals ({', '.join(column_headers)}) VALUES "

        # Append each data line to the SQL query
        for line in data_lines:
            values = line.split('\t')
            formatted_values = [f"'{value}'" if (value and value!='None') else 'NULL' for value in values]
            sql_query += f"({', '.join(formatted_values)}), "
        
        # Remove the trailing comma and execute the SQL query
        sql_query = sql_query.rstrip(', ')
        cur = db.get_db().cursor()
        cur.execute(sql_query)
        db.get_db().commit()
        cur.close()

        return {"status":"Principals added"}, 200

class TitleRatings(Resource):
    @login_required
    @admin_required
    def post(self, user):
        tsv_data = request.form.get("tsv_data")
        # Split the TSV data into lines
        lines = tsv_data.strip().split('\n')

        # Extract column headers and data
        column_headers = lines[0].split('\t')
        data_lines = lines[1:]

        # Create the SQL query for inserting data into the specified table
        sql_query = f"INSERT IGNORE INTO imdb_rating ({', '.join(column_headers)}) VALUES "

        # Append each data line to the SQL query
        for line in data_lines:
            values = line.split('\t')
            formatted_values = [f"'{value}'" if (value and value!='None') else 'NULL' for value in values]
            sql_query += f"({', '.join(formatted_values)}), "
        
        # Remove the trailing comma and execute the SQL query
        sql_query = sql_query.rstrip(', ')
        cur = db.get_db().cursor()
        cur.execute(sql_query)
        db.get_db().commit()
        cur.close()

        return {"status":"Ratings added"}, 200
    
class ResetAll(Resource):
    @login_required
    @admin_required
    def post(self, user):
        return {"message": "Reset All"}

class UserMod(Resource):
    @login_required
    @admin_required
    def post(self, user, username, password):
        # Check if the user already exists
        cur = db.get_db().cursor()
        cur.execute("SELECT username FROM app_user WHERE username=%s", [username])
        user_check = cur.fetchone()
        cur.close()

        if user_check:
            # User exists, update the password
            cur = db.get_db().cursor()
            cur.execute("UPDATE app_user SET password=%s WHERE username=%s", [password, username])
            db.get_db().commit()
            cur.close()

            return {'message': f'Password for user {username} updated successfully'}, 200

        # create new token for the new user
        token = secrets.token_hex(16)

        # Add user to the database
        cur = db.get_db().cursor()
        cur.execute("INSERT IGNORE INTO app_user (user_role, token, first_name, last_name, birthdate, email, username, password) \
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s )",
                    ('standard_user',token,  None , None , None, None, username, password))
        db.get_db().commit()
        cur.close()

        return {'message': f'User {username} created successfully'}, 201

class UserInfo(Resource):
    @login_required
    @admin_required
    def get(self, user, username):
        # Check if the target user exists
        cur = db.get_db().cursor()
        cur.execute("SELECT * FROM app_user WHERE username=%s", [username])
        target_user_data = cur.fetchone()
        cur.close()

        if not target_user_data:
            return {'error': f'User {username} not found'}, 404

        # Format and return user information
        user_info = {
            'username': target_user_data["username"],
            'user_role': target_user_data["user_role"],
            'first_name': target_user_data["first_name"],
            'last_name': target_user_data["last_name"],
            'birthdate': str(target_user_data["birthdate"]),
            'email': target_user_data["email"]
            # Add other fields if needed
        }
        json_result = json.dumps(user_info, sort_keys=False)
        response = make_response(json_result, 200)
        return response
