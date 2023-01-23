from flask import render_template, request

from app.search import bp


@bp.route('/text', methods=['GET', 'POST'])
def text():
    if request.method == 'POST':
        get_text = request.form['text']
        print(get_text)
    
    return render_template('search/text.html')
