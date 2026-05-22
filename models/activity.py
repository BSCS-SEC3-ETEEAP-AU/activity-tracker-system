from extensions import db
from datetime import datetime

class Activity(db.Model):
    __tablename__ = 'activities'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    task_name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)
    hours_rendered = db.Column(db.Float)
    activity_date = db.Column(db.DateTime, default=datetime.utcnow)