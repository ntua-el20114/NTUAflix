from flask import Blueprint, render_template, session, flash, redirect
import requests

catalogue = Blueprint('Catalogue', __name__)

@catalogue.route('/Catalogue', methods=['GET'])
def show():
    # If not logged in, redirect to welcome page
    if 'user_token' not in session:
        return redirect('/')

    # Get liked movies
    recommended = []
    url = 'http://127.0.0.1:9876/ntuaflix_api/getlikedmovies'
    response = requests.get(url, headers = {'X-OBSERVATORY-AUTH': session['user_token']})
    if response.status_code == 200:
        too_long = False
        # Get recommendations based on each movie
        for movie in response.json()["result"]:
            if too_long: break
            url = f'http://127.0.0.1:9876/ntuaflix_api/movierecommender_1/{movie["originalTitle"]}'
            response = requests.get(url, headers = {'X-OBSERVATORY-AUTH': session['user_token']})
            try:
                for title in response.json()['result']:
                    if too_long: break
                    # avoid duplicate movies
                    exists = False
                    for rec in recommended:
                        if rec['id'] == title['titleID']:
                            exists = True
                            break
                    if not exists: recommended.append({"title": title["originalTitle"], "thumbnail": title["titlePoster"], "id": title["titleID"]})
                    
                    # If recommendations list gets too long, keep only the best rec for each movie
                    if len(recommended) > 30: break
                    
                    # If recommendations list gets way too long, break completely
                    # This is done to handle edge cases where the user has a very large amount of liked movies
                    if len(recommended) >= 60:
                        too_long = True
                        break
            except:
                continue
    else:
        flash("There was an error getting recommended movies", "error")

    # Get top rated movies
    url = 'http://127.0.0.1:9876/ntuaflix_api/gettopratedmovies'
    response = requests.get(url, headers = {'X-OBSERVATORY-AUTH': session['user_token']})
    if response.status_code == 200:
        top_rated = [{"title": movie["originalTitle"], "thumbnail": movie["titlePoster"], "id": movie["titleID"]} 
            for movie in response.json()["result"]]
    else:
        flash("There was an error getting top rated movies", "error")
    return render_template('Catalogue.html', top_rated=top_rated, recommended=recommended)