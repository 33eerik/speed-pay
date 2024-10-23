from flask import render_template, request, flash, redirect, url_for, send_file
<<<<<<< HEAD
from app import db
=======
from app import app, db
>>>>>>> origin/main
from models import Contact, Lead
from forms import ContactForm, LeadForm
import os

<<<<<<< HEAD
def index():
    return render_template('index.html')

def services():
    return render_template('services.html')

def about():
    return render_template('about.html')

=======
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
>>>>>>> origin/main
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        new_contact = Contact(name=form.name.data, email=form.email.data, message=form.message.data)
        db.session.add(new_contact)
        db.session.commit()
        flash('Your message has been sent. We will get back to you soon!', 'success')
        return redirect(url_for('index'))
    return render_template('contact.html', form=form)

<<<<<<< HEAD
=======
@app.route('/landing', methods=['GET', 'POST'])
>>>>>>> origin/main
def landing_page():
    form = LeadForm()
    if form.validate_on_submit():
        new_lead = Lead(name=form.name.data, email=form.email.data, company=form.company.data, phone=form.phone.data)
        db.session.add(new_lead)
        db.session.commit()
        flash('Thank you for your interest! We\'ll be in touch shortly.', 'success')
        return redirect(url_for('thank_you'))
    return render_template('landing.html', form=form)

<<<<<<< HEAD
def thank_you():
    return render_template('thank_you.html')

def download_ebook():
    email = request.form.get('email')
    if email:
=======
@app.route('/thank-you')
def thank_you():
    return render_template('thank_you.html')

@app.route('/download-ebook', methods=['POST'])
def download_ebook():
    email = request.form.get('email')
    if email:
        # Save the email to the database (you might want to create a new model for this)
>>>>>>> origin/main
        new_lead = Lead(name="E-book Subscriber", email=email, company="Unknown", phone="Unknown")
        db.session.add(new_lead)
        db.session.commit()
        
<<<<<<< HEAD
        ebook_path = os.path.join('static', 'ebook.txt')
=======
        # Send the e-book
        # For demonstration purposes, we'll just send a text file
        # In a real scenario, you'd have an actual e-book file to send
        ebook_path = os.path.join(app.root_path, 'static', 'ebook.txt')
>>>>>>> origin/main
        return send_file(ebook_path, as_attachment=True, attachment_filename='10_strategies_for_efficient_payment_processing.txt')
    else:
        flash('Please provide a valid email address.', 'error')
        return redirect(url_for('index'))
