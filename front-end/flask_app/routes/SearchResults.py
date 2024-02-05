from flask import Blueprint, render_template, session, redirect, request, flash
import requests

search_results = Blueprint('SearchResults', __name__)

@search_results.route('/SearchResults', methods=['GET'])
def show():
    # If not logged in, redirect to welcome page
    if 'user_token' not in session:
        return redirect('/')

    query = request.args.get('query')
    results = []

    # Make the request
    url = 'http://127.0.0.1:9876/ntuaflix_api/searchtitle'
    data = {'titlePart': query}
    response = requests.get(url, headers = {'X-OBSERVATORY-AUTH': session['user_token']},data=data)
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        for movie in response.json()["result"]:
            results.append({"title": movie["originalTitle"], "thumbnail": movie["titlePoster"], "id": movie["titleID"]})
    elif response.status_code == 204:
        flash("No movies found", "warning")
    else:
        flash("There was an error getting search results", "error")

    return render_template('SearchResults.html', query=query, results=results)