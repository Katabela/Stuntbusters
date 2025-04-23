import os

class Config:
    ENV = os.getenv("ENV")
    FLASK_ENV = os.getenv("FLASK_ENV")
    FLASK_APP = os.getenv("FLASK_APP")
    DEBUG = ENV == "development"

    SECRET_KEY = os.getenv("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    DOMAIN_URL = os.getenv("DOMAIN_URL")

    # Gmail API OAuth2 Credentials
    GMAIL_CLIENT_ID = os.getenv("GMAIL_CLIENT_ID")
    GMAIL_CLIENT_SECRET = os.getenv("GMAIL_CLIENT_SECRET")
    GMAIL_REFRESH_TOKEN = os.getenv("GMAIL_REFRESH_TOKEN")