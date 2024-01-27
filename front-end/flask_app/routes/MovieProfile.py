from flask import Blueprint, render_template

movie_profile = Blueprint('MovieProfile', __name__)

@movie_profile.route('/MovieProfile')
def show():
    return render_template('MovieProfile.html')