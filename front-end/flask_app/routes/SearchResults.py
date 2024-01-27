from flask import Blueprint, render_template

search_results = Blueprint('SearchResults', __name__)

@search_results.route('/SearchResults')
def show():
    return render_template('SearchResults.html')