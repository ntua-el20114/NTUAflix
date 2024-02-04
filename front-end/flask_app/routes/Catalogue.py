from flask import Blueprint, render_template, session, flash
import requests

catalogue = Blueprint('Catalogue', __name__)

@catalogue.route('/Catalogue', methods=['GET'])
def show():
    # Get top rated movies !-Not working
    url = 'http://127.0.0.1:9876/ntuaflix_api/gettopratedmovies'
    response = requests.get(url, headers = {'X-OBSERVATORY-AUTH': session['user_token']})
    if response.status_code == 200:
        print("Successfully got top rated movies")
        top_rated = [{"title": movie["originalTitle"], "thumbnail": movie["titlePoster"], "id": movie["titleID"]} 
            for movie in response.json()["result"]]
        print(top_rated)
    else:
        flash("There was an error getting top rated movies", "error")
    return render_template('Catalogue.html', top_rated=top_rated)