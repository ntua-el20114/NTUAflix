from flask import Blueprint, render_template, flash, session
import requests
import json

movie_profile = Blueprint('MovieProfile', __name__)

@movie_profile.route('/MovieProfile/<string:titleID>')
def show(titleID):
    # Get Movie Info
    url = 'http://127.0.0.1:9876/ntuaflix_api/title/' + titleID
    response = requests.get(url, headers = {'X-OBSERVATORY-AUTH': session['user_token']})
    if response.status_code == 200:
        print("Successfully got movie info")
        print(json.dumps(response.json(), indent=4))
        movie_info = response.json()
        # Organize movie principals
        movie_info['principals'] = {}
        movie_info['principals']['Directors'] = [principal['name'] for principal in response.json()['principals'] if principal['category'] == 'director']
        movie_info['principals']['Producers'] = [principal['name'] for principal in response.json()['principals'] if principal['category'] == 'producer']
        movie_info['principals']['Actors'] = [principal['name'] for principal in response.json()['principals'] if principal['category'] == 'actor' or principal['category'] == 'actress']
        movie_info['principals']['Cinematographers'] = [principal['name'] for principal in response.json()['principals'] if principal['category'] == 'cinematographer']
        movie_info['principals']['Editors'] = [principal['name'] for principal in response.json()['principals'] if principal['category'] == 'editor']
        movie_info['principals']['Composers'] = [principal['name'] for principal in response.json()['principals'] if principal['category'] == 'composer']
        movie_info['principals']['Production Designers'] = [principal['name'] for principal in response.json()['principals'] if principal['category'] == 'production_designer']
        movie_info['principals']['Writers'] = [principal['name'] for principal in response.json()['principals'] if principal['category'] == 'writer']
        print(movie_info)
    else:
        flash("There was an error getting movie info", "error")
        movie_info = None
    return render_template('MovieProfile.html', movie=movie_info)