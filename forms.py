from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, TextAreaField, SelectField, SubmitField
from wtforms.validators import DataRequired, Email, Length, Optional


class EmployerLeadForm(FlaskForm):
    name = StringField('Your Name', validators=[DataRequired(), Length(min=2, max=100)])
    company = StringField('Company Name', validators=[DataRequired(), Length(min=2, max=200)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    phone = StringField('Phone Number', validators=[DataRequired(), Length(min=10, max=20)])
    industry = SelectField('Industry', choices=[
        ('hospitality', 'Hospitality'),
        ('industrial', 'Industrial'),
        ('general_labor', 'General Labor'),
        ('administrative', 'Administrative'),
        ('other', 'Other')
    ], validators=[DataRequired()])
    staffing_needs = TextAreaField('Describe Your Staffing Needs', validators=[DataRequired()])
    submit = SubmitField('Get Staffed Fast')


class CandidateApplicationForm(FlaskForm):
    name = StringField('Your Name', validators=[DataRequired(), Length(min=2, max=100)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    phone = StringField('Phone Number', validators=[DataRequired(), Length(min=10, max=20)])
    position_type = SelectField('Position Type', choices=[
        ('hospitality', 'Hospitality'),
        ('industrial', 'Industrial'),
        ('general_labor', 'General Labor'),
        ('administrative', 'Administrative'),
        ('other', 'Other')
    ], validators=[DataRequired()])
    availability = StringField('When Are You Available to Start?', validators=[DataRequired()])
    experience = TextAreaField('Brief Description of Your Experience', validators=[DataRequired()])
    resume = FileField('Upload Resume (PDF, DOC, DOCX - Optional)', 
                       validators=[Optional(), FileAllowed(['pdf', 'doc', 'docx'], 'PDF, DOC, or DOCX files only')])
    submit = SubmitField('Apply Now')
