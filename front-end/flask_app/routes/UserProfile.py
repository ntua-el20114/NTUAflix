from flask import Blueprint, render_template, redirect, session, flash
import requests

user_profile = Blueprint('UserProfile', __name__)

@user_profile.route('/UserProfile', methods=['GET'])
def show():
    # If not logged in, redirect to welcome page
    if 'user_token' not in session:
        return redirect('/')

    # Get Liked Movies
    url = 'http://127.0.0.1:9876/ntuaflix_api/getlikedmovies'
    response = requests.get(url, headers = {'X-OBSERVATORY-AUTH': session['user_token']})
    if response.status_code == 200:
        print("Successfully got liked movies")
        # Keep only essensial data
        liked_movies = [{"title": movie["originalTitle"], "thumbnail": movie["titlePoster"], "id": movie["titleID"]} 
                        for movie in response.json()["result"]]
        print(liked_movies)
    else:
        flash("There was an error getting liked movies", "error")

    # Get Disliked Movies
    url = 'http://127.0.0.1:9876/ntuaflix_api/getdislikedmovies'
    response = requests.get(url, headers = {'X-OBSERVATORY-AUTH': session['user_token']})
    if response.status_code == 200:
        print("Successfully got disliked movies")
        disliked_movies = [{"title": movie["originalTitle"], "thumbnail": movie["titlePoster"], "id": movie["titleID"]}
                           for movie in response.json()["result"]]
        print(disliked_movies)
    else:
        flash("There was an error getting disliked movies", "error")
    

    return render_template('UserProfile.html', 
                           liked_movies=liked_movies, disliked_movies=disliked_movies)

@user_profile.route('/UserProfile', methods=['POST'])
def logout():
    url = 'http://127.0.0.1:9876/ntuaflix_api/logout'
    response = requests.post(url, headers = {'X-OBSERVATORY-AUTH': session['user_token']})
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        print("Successfully logged out")
        print(response.text)
    else:
        print(f'Error: {response.status_code}')

    session.clear()
    return redirect("/")