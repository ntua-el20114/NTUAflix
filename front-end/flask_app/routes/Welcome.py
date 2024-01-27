from flask import Blueprint, render_template

welcome = Blueprint('Welcome', __name__)

@welcome.route('/')
def show():
    return render_template('Welcome.html')