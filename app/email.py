import base64
import os
import smtplib
from email.mime.text import MIMEText
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request

def send_oauth_email(to_email, subject, body_text):
    # Load Gmail OAuth2 credentials from .env
    CLIENT_ID = os.getenv("GMAIL_CLIENT_ID")
    CLIENT_SECRET = os.getenv("GMAIL_CLIENT_SECRET")
    REFRESH_TOKEN = os.getenv("GMAIL_REFRESH_TOKEN")

    creds = Credentials(
        None,
        refresh_token=REFRESH_TOKEN,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        token_uri='https://oauth2.googleapis.com/token'
    )

    creds.refresh(Request())  # Get access token using refresh token

    access_token = creds.token
    auth_string = f'user={os.getenv("MAIL_USERNAME")}\1auth=Bearer {access_token}\1\1'
    auth_string = base64.b64encode(auth_string.encode("utf-8")).decode("utf-8")

    # Build and send the email
    message = MIMEText(body_text)
    message["to"] = to_email
    message["from"] = os.getenv("MAIL_USERNAME")
    message["subject"] = subject

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.ehlo()
        server.starttls()
        server.docmd("AUTH", "XOAUTH2 " + auth_string)
        server.sendmail(
            os.getenv("MAIL_USERNAME"),
            to_email,
            message.as_string()
        )
