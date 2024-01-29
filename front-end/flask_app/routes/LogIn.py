from flask import Blueprint, render_template, request, flash, redirect, session
import requests

login = Blueprint('Login', __name__)

@login.route('/Login', methods=['GET'])
def show():
    return render_template('LogIn.html')

@login.route('/Login', methods=['POST'])
def login_submit():
    username = request.form['username']
    password = request.form['password']

    if username=="" or password=="":
        flash("Please provide a username and a password", "error")
        return redirect("/Login")

    print(f"Logging in as {username} with password {password}")
    url = 'http://127.0.0.1:9876/ntuaflix_api/login'
    data = {'username': username, 'password': password}
    response = requests.post(url, data=data)

    if response.status_code == 200:        
        # Store user token in session
        session['user_token'] = response.json()['token']

        # Store user data in session
        url='http://127.0.0.1:9876/ntuaflix_api/getappuserdata'
        usr_data = requests.get(url, headers={ 'X-OBSERVATORY-AUTH': session['user_token']})
        session['username'] = username
        session['first_name'] = usr_data.json()['first_name']
        session['last_name'] = usr_data.json()['last_name']
        session['email'] = usr_data.json()['email']
        session['birthdate'] = usr_data.json()['birthdate']
        return redirect("/Catalogue")

    else:
        flash("Username or password was incorrect", "error")

    return redirect("/Login")