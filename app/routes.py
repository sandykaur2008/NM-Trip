from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')


@app.route('/about')
def about():
    return render_template('about.html', title='About')


@app.route('/contact')
def contact():
    return render_template('contact.html', title='Contact')


@app.route('/carlsbad')
def carlsbad():
    return render_template('carlsbad.html', title='Carlsbad')


@app.route('/food')
def food():
    return render_template('food.html', title='Food')


@app.route('/road')
def road():
    return render_template('road.html', title='The Road')


@app.route('/whitesands')
def whitesands():
    return render_template('whitesands.html', title='White Sands')