from flask import Blueprint, render_template

catalogue = Blueprint('Catalogue', __name__)

@catalogue.route('/Catalogue')
def show():
    return render_template('Catalogue.html')