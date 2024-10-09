from flask import render_template, request, flash, redirect, url_for
from app import app, db
from models import Contact
from forms import ContactForm

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        new_contact = Contact(name=form.name.data, email=form.email.data, message=form.message.data)
        db.session.add(new_contact)
        db.session.commit()
        flash('Your message has been sent. We will get back to you soon!', 'success')
        return redirect(url_for('index'))
    return render_template('contact.html', form=form)
