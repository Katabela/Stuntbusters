from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, FileField
from wtforms.validators import DataRequired, Email

class StuntForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    skill_name = StringField('Skill Name', validators=[DataRequired()])
    issue_desc = TextAreaField('Issue Description', validators=[DataRequired()])
    flyer_view = TextAreaField("Flyer’s View")
    base_view = TextAreaField("Base’s View")
    video1 = FileField('Video 1')
    video2 = FileField('Video 2')
    video3 = FileField('Video 3')