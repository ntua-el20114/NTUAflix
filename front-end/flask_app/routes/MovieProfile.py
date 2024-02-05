from flask import Blueprint, render_template, flash, session, redirect
import requests
import json

movie_profile = Blueprint('MovieProfile', __name__)

@movie_profile.route('/MovieProfile/<string:titleID>', methods=['GET'])
def show(titleID):
    # If not logged in, redirect to welcome page
    if 'user_token' not in session:
        return redirect('/')

    if session["movie_profile_first_visit"]:
        flash("Hint: click on a person's name to view their profile", "info")
        session["movie_profile_first_visit"] = False

    # Determine whether user has liked movie
    liked = False
    url = 'http://127.0.0.1:9876/ntuaflix_api/getlikedmovies'
    response = requests.get(url, headers = {'X-OBSERVATORY-AUTH': session['user_token']})
    if response.status_code == 200:
        for movie in response.json()["result"]:
            if movie["titleID"] == titleID:
                liked = True
                break
    
    # Determine whether user has disliked movie
    disliked = False
    url = 'http://127.0.0.1:9876/ntuaflix_api/getdislikedmovies'
    response = requests.get(url, headers = {'X-OBSERVATORY-AUTH': session['user_token']})
    if response.status_code == 200:
        for movie in response.json()["result"]:
            if movie["titleID"] == titleID:
                disliked = True
                break

    # Get Movie Info
    url = 'http://127.0.0.1:9876/ntuaflix_api/title/' + titleID
    response = requests.get(url, headers = {'X-OBSERVATORY-AUTH': session['user_token']})
    if response.status_code == 200:
        # print(json.dumps(response.json(), indent=4))
        movie_info = response.json()
        # Organize movie principals
        movie_info['principals'] = {}
        movie_info['principals']['Directors'] = [{'id': principal['nameID'], 'name': principal['name']} for principal in response.json()['principals'] if principal['category'] == 'director'] if response.json()['principals']!='None' else []
        movie_info['principals']['Producers'] = [{'id': principal['nameID'], 'name': principal['name']} for principal in response.json()['principals'] if principal['category'] == 'producer'] if response.json()['principals']!='None' else []
        movie_info['principals']['Actors'] = [{'id': principal['nameID'], 'name': principal['name']} for principal in response.json()['principals'] if principal['category'] == 'actor' or principal['category'] == 'actress'] if response.json()['principals']!='None' else []
        movie_info['principals']['Cinematographers'] = [{'id': principal['nameID'], 'name': principal['name']} for principal in response.json()['principals'] if principal['category'] == 'cinematographer'] if response.json()['principals']!='None' else []
        movie_info['principals']['Editors'] = [{'id': principal['nameID'], 'name': principal['name']} for principal in response.json()['principals'] if principal['category'] == 'editor'] if response.json()['principals']!='None' else []
        movie_info['principals']['Composers'] = [{'id': principal['nameID'], 'name': principal['name']} for principal in response.json()['principals'] if principal['category'] == 'composer'] if response.json()['principals']!='None' else []
        movie_info['principals']['Production Designers'] = [{'id': principal['nameID'], 'name': principal['name']} for principal in response.json()['principals'] if principal['category'] == 'production_designer'] if response.json()['principals']!='None' else []
        movie_info['principals']['Writers'] = [{'id': principal['nameID'], 'name': principal['name']} for principal in response.json()['principals'] if principal['category'] == 'writer'] if response.json()['principals']!='None' else []
    else:
        flash("There was an error getting movie info", "error")
        movie_info = None
    return render_template('MovieProfile.html', movie=movie_info, liked=liked, disliked=disliked)