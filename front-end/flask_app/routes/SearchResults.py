from flask import Blueprint, render_template, session, redirect

search_results = Blueprint('SearchResults', __name__)

@search_results.route('/SearchResults')
def show():
    # If not logged in, redirect to welcome page
    if 'user_token' not in session:
        return redirect('/')

    return render_template('SearchResults.html')