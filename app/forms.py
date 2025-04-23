from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, FileField
from wtforms.validators import DataRequired, Email

class StuntForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    skill_name = StringField("Skill Name", validators=[DataRequired()])
    issue_desc = TextAreaField("Describe the Issue", validators=[DataRequired()])
    flyer_view = TextAreaField("Flyer's Perspective", validators=[DataRequired()])
    base_view = TextAreaField("Base's Perspective", validators=[DataRequired()])
    
    video_1 = FileField("Upload Video 1")
    video_2 = FileField("Upload Video 2")
    video_3 = FileField("Upload Video 3")