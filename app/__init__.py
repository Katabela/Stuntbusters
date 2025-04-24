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

     # Load configurations based on the environment
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URI")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["DEBUG"] = environment == "development"
    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")

    db.init_app(app)
    mail.init_app(app)
    csrf.init_app(app)

    from .routes import main
    app.register_blueprint(main)

    from . import models

    return app
