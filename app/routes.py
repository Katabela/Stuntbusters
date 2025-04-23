from flask import Blueprint, render_template, redirect, url_for, request
from .forms import StuntForm
from .models import db, User, StuntSubmission
from flask_mail import Message
from .email import send_oauth_email
from . import mail

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('home.html')

@main.route('/submit', methods=['GET', 'POST'])
def submit():
    form = StuntForm()
    if form.validate_on_submit():
        email = form.email.data

        # Create or get user
        user = User.query.filter_by(email=email).first()
        if not user:
            user = User(email=email)
            db.session.add(user)
            db.session.commit()

        submission = StuntSubmission(
            user_id=user.id,
            skill_name=form.skill_name.data,
            issue_desc=form.issue_desc.data,
            flyer_view=form.flyer_view.data,
            base_view=form.base_view.data,
            video_1="video1.mp4",  # placeholder for now
            video_2="video2.mp4",
            video_3="video3.mp4"
        )
        db.session.add(submission)
        db.session.commit()

        # Send confirmation email
        send_oauth_email(
            to_email=email,
            subject="Stunt Fix Request Submitted",
            body_text="Thanks for submitting your Stunt Fix request! We'll get back to you within two days."
        )

        return redirect(url_for('main.thank_you'))

    return render_template('form.html', form=form)

@main.route('/thank-you')
def thank_you():
    return render_template('thank_you.html')