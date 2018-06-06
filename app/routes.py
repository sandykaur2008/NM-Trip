from flask import render_template, url_for, flash, redirect 
from app import app
from app.forms import ContactForm
from app.email import send_email

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')


@app.route('/about')
def about():
    return render_template('about.html', title='About')


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        send_email('NM Trip - Feedback', sender=app.config['MAIL_USERNAME'],
        recipients=['sandykaur2008@gmail.com'], text_body="""
        From: {} <{}>
        {}
        """.format(form.name.data, form.email.data, form.text.data))
        flash('Thank you for your input, {}!'.format(form.name.data))
        return redirect(url_for('index'))
    return render_template('contact.html', title='Contact', form=form)


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