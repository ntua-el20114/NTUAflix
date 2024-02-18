from flask import Blueprint, render_template, session, flash, redirect, request, jsonify
import requests

bygenre = Blueprint('ByGenre', __name__)


@bygenre.route('/ByGenre', methods=['GET'])
def show():
    # If not logged in, redirect to welcome page
    if 'user_token' not in session:
        return redirect('/')

    # Get the genre from the query parameters
    qgenre = request.args.get('qgenre')

    minrating = 0
    yrFrom = 1000
    yrTo = 3000

    print(f"Received minrating parameter: {minrating}") ##ok

    # Get movies
    movies1 = []
    url = 'http://127.0.0.1:9876/ntuaflix_api/bygenre'
    data = {'qgenre': qgenre, 'minrating': minrating, 'yrFrom':yrFrom, 'yrTo': yrTo}
    response = requests.get(url, headers = {'X-OBSERVATORY-AUTH': session['user_token']}, data=data)
    #print(f"Response: {response.text}") 

    if response.status_code == 200:
        movies1 = [{"title": movie["originalTitle"], "thumbnail": movie["titlePoster"], "id": movie["title_id"]} 
            for movie in response.json()["result"]]
    else:
        flash("There was an error getting by genre movies", "error")
    return render_template('ByGenre.html', movies1=movies1)

    # if response.status_code == 200:
    #     too_long = False
    #     # Get movies
    #     for movie in response.json()["result"]:
    #         if too_long: break
    #         url = f'http://127.0.0.1:9876/ntuaflix_api/bygenre/{movie["originalTitle"]}'
    #         response = requests.get(url, headers = {'X-OBSERVATORY-AUTH': session['user_token']})
    #         try:
    #             for title in response.json()['result']:
    #                 if too_long: break
    #                 # avoid duplicate movies
    #                 exists = False
    #                 for rec in movies1:
    #                     if rec['id'] == title['titleID']:
    #                         exists = True
    #                         break
    #                 if not exists: movies1.append({"tit   le": title["originalTitle"], "thumbnail": title["titlePoster"], "id": title["titleID"]})
                    
    #                 # If recommendations list gets too long, keep only the best rec for each movie
    #                 if len(movies1) > 60: break
                    
    #                 # If recommendations list gets way too long, break completely
    #                 # This is done to handle edge cases where the user has a very large amount of liked movies
    #                 if len(movies1) >= 100:
    #                     too_long = True
    #                     break
    #         except:
    #             continue

    #     return render_template('ByGenre.html', movies1=movies1)
    #     result2 = {'result': [{'title': 'Movie 1'}, {'title': 'Movie 2'}]}
    #     return jsonify(result2)

    # else:
    #     flash("There was an error getting movies by genre", "error")

    # return render_template('ByGenre.html', recommended=movies1)
    # result3 = {'result': [{'title': 'Movie 1'}, {'title': 'Movie 2'}]}
    # return jsonify(result3)
