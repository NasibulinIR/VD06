from flask import render_template, request, redirect, url_for
from my_app import app

cards = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        title = request.form['title']
        town = request.form['town']
        hobby = request.form['hobby']
        age = request.form['age']
        if title and town and hobby and age:
            cards.append({
                'title': title,
                'town': town,
                'hobby': hobby,
                'age': age
            })
            return redirect(url_for('index'))
    return render_template('form-cards.html', cards=cards)