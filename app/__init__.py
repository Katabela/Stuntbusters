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
    app.config.from_object(Config)

    db.init_app(app)
    mail.init_app(app)
    csrf.init_app(app)

    from .routes.main_routes import main
    app.register_blueprint(main)

    from . import models

    return app
