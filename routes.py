import logging
from flask import render_template, request, redirect, url_for, flash
from app import app, db
from forms import EmployerLeadForm, CandidateApplicationForm
from models import EmployerLead, CandidateApplication
from utils import send_notification_email

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
    employer_form = EmployerLeadForm()
    candidate_form = CandidateApplicationForm()
    
    form_type = request.args.get('form_type', 'employer')
    
    return render_template(
        'contact.html',
        employer_form=employer_form,
        candidate_form=candidate_form,
        form_type=form_type
    )

@app.route('/submit_employer', methods=['POST'])
def submit_employer():
    form = EmployerLeadForm()
    
    if form.validate_on_submit():
        try:
            new_lead = EmployerLead(
                name=form.name.data,
                company=form.company.data,
                email=form.email.data,
                phone=form.phone.data,
                industry=form.industry.data,
                staffing_needs=form.staffing_needs.data
            )
            
            db.session.add(new_lead)
            db.session.commit()
            
            # Send notification email to staff
            send_notification_email(
                subject="New Employer Lead Submitted",
                body_text=f"New lead from {form.name.data} at {form.company.data}.\nIndustry: {form.industry.data}\nContact: {form.email.data}, {form.phone.data}\nNeeds: {form.staffing_needs.data}"
            )
            
            flash('Your staffing request has been received. We will contact you shortly!', 'success')
            return redirect(url_for('success', type='employer'))
            
        except Exception as e:
            logging.error(f"Error saving employer lead: {e}")
            db.session.rollback()
            flash('There was an error processing your request. Please try again.', 'danger')
    else:
        for field, errors in form.errors.items():
            for error in errors:
                flash(f"{getattr(form, field).label.text}: {error}", 'danger')
    
    return redirect(url_for('contact', form_type='employer'))

@app.route('/submit_candidate', methods=['POST'])
def submit_candidate():
    form = CandidateApplicationForm()
    
    if form.validate_on_submit():
        try:
            new_application = CandidateApplication(
                name=form.name.data,
                email=form.email.data,
                phone=form.phone.data,
                position_type=form.position_type.data,
                availability=form.availability.data,
                experience=form.experience.data
            )
            
            db.session.add(new_application)
            db.session.commit()
            
            # Send notification email to staff
            send_notification_email(
                subject="New Candidate Application Submitted",
                body_text=f"New application from {form.name.data}.\nPosition: {form.position_type.data}\nContact: {form.email.data}, {form.phone.data}\nAvailability: {form.availability.data}\nExperience: {form.experience.data}"
            )
            
            flash('Your application has been received. Our team will review it and contact you soon!', 'success')
            return redirect(url_for('success', type='candidate'))
            
        except Exception as e:
            logging.error(f"Error saving candidate application: {e}")
            db.session.rollback()
            flash('There was an error processing your application. Please try again.', 'danger')
    else:
        for field, errors in form.errors.items():
            for error in errors:
                flash(f"{getattr(form, field).label.text}: {error}", 'danger')
    
    return redirect(url_for('contact', form_type='candidate'))

@app.route('/success')
def success():
    submission_type = request.args.get('type', 'employer')
    return render_template('success.html', submission_type=submission_type)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def server_error(e):
    return render_template('500.html'), 500
