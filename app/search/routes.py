from flask import render_template, render_template_string, request

from app.search import bp
from app.models.intervenants import Intervenants



@bp.route('/')
def index():
    return render_template('search/recherche_textuelle.html')


@bp.route('/active_search', methods=['POST'])
def active_search():
    
    search = request.form['search']
    intervs = Intervenants.objects.search_text(search).order_by('$text_score')


    return render_template('search/results.html', intervs=intervs)


@bp.route('/combinaison')
def combinaison():

    return render_template('search/combinaison.html')
