from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from flask_wtf.csrf import CSRFProtect
from instance.config import Config
import os

db = SQLAlchemy()
mail = Mail()
csrf = CSRFProtect()

def create_app(environment="production"):
    app = Flask(__name__, instance_relative_config=True)

     # Base Config from .env
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("SQLALCHEMY_DATABASE_URI")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "dev-secret")
    app.config["DEBUG"] = environment == "development"
    app.config["DOMAIN_URL"] = os.getenv("DOMAIN_URL")

    # Gmail API Credentials
    app.config["MAIL_USERNAME"] = os.getenv("MAIL_USERNAME")
    app.config["GMAIL_CLIENT_ID"] = os.getenv("GMAIL_CLIENT_ID")
    app.config["GMAIL_CLIENT_SECRET"] = os.getenv("GMAIL_CLIENT_SECRET")
    app.config["GMAIL_REFRESH_TOKEN"] = os.getenv("GMAIL_REFRESH_TOKEN")

    db.init_app(app)
    mail.init_app(app)
    csrf.init_app(app)

    from .routes.main_routes import main
    app.register_blueprint(main)

    from . import models

    return app
