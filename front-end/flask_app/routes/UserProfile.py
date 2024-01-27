from flask import Blueprint, render_template, redirect, session
import requests

user_profile = Blueprint('UserProfile', __name__)

@user_profile.route('/UserProfile', methods=['GET'])
def show():
    return render_template('UserProfile.html')

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