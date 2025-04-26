from datetime import datetime
from app import db

class EmployerLead(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    company = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    industry = db.Column(db.String(50), nullable=False)
    staffing_needs = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<EmployerLead {self.name} - {self.company}>'


class CandidateApplication(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    position_type = db.Column(db.String(50), nullable=False)
    availability = db.Column(db.String(100), nullable=False)
    experience = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<CandidateApplication {self.name} - {self.position_type}>'
