from flask import render_template, request, Blueprint
from .search import search_function

search_bp = Blueprint('search', __name__)

@search_bp.route('/search', methods=['POST'])
def search():
    if request.method == 'POST':
        query = request.form.get('search_query')
        results = search_function(query)
        return render_template('search_results.html', results=results)
