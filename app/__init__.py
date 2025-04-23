from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from flask_wtf.csrf import CSRFProtect
from instance.config import Config

db = SQLAlchemy()
mail = Mail()
csrf = CSRFProtect()

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(Config)

    db.init_app(app)
    mail.init_app(app)
    csrf.init_app(app)

    from .routes import main
    app.register_blueprint(main)

    return app