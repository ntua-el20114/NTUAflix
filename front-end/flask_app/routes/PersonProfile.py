from flask import Blueprint, render_template, flash, session
import requests
import json

person_profile = Blueprint('PersonProfile', __name__)

@person_profile.route('/PersonProfile/<string:nameID>', methods=['GET'])
def show(nameID):
    # Get person info
    url = 'http://127.0.0.1:9876/ntuaflix_api/name/' + nameID
    response = requests.get(url, headers = {'X-OBSERVATORY-AUTH': session['user_token']})
    if response.status_code == 200:
        print(json.dumps(response.json(), indent=4))
        # Organize data
        person = response.json()
        if person['birthYr'] != 'Null': person['birthYr']=str(person['birthYr'])
        if person['deathYr'] != 'Null': person['deathYr']=str(person['deathYr'])
        if person['profession'] != 'Null': person['profession'] = person['profession'].replace('_', ' ').split(',')
        if person['nameTitles'] != 'Null':
            # Get title names
            for title in person['nameTitles']:
                url = url = 'http://127.0.0.1:9876/ntuaflix_api/title/' + title['title_id']
                response = requests.get(url, headers = {'X-OBSERVATORY-AUTH': session['user_token']})
                if response.status_code == 200:
                    title['name'] = response.json()['originalTitle']
                else:
                    title['name'] = '[Error getting title name]'
    else:
        flash("There was an error getting person info", "error")
        print(response)
        person=None
    return render_template('PersonProfile.html', id=nameID, person=person, movie=None)