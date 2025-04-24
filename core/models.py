from . import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    submissions = db.relationship('StuntSubmission', backref='user', lazy=True)

class StuntSubmission(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    skill_name = db.Column(db.String(100))
    issue_desc = db.Column(db.Text)
    flyer_view = db.Column(db.Text)
    base_view = db.Column(db.Text)
    video_1 = db.Column(db.String(200))
    video_2 = db.Column(db.String(200))
    video_3 = db.Column(db.String(200))