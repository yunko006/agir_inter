from flask import render_template, request

from app.search import bp
from app.models.intervenants import Intervenants


@bp.route('/text', methods=['GET', 'POST'])
def text():
    if request.method == 'POST':
        search = request.form['text']

        result_search = Intervenants.objects.search_text(search).order_by('$text_score')

        return render_template('search/text-results.html', results=result_search)


    return render_template('search/text.html')
