from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from flask_wtf.csrf import CSRFProtect
from dotenv import load_dotenv
from livereload import Server
import os

# Load environment variables from .env file
load_dotenv(override=True)

# Create the Flask app
app = Flask(__name__, template_folder="app/templates", static_folder="app/static")

# Set config values directly from environment
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("SQLALCHEMY_DATABASE_URI")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")

# Initialize extensions
db = SQLAlchemy(app)
mail = Mail(app)
csrf = CSRFProtect(app)

# Import and register blueprints
from app.routes import main
app.register_blueprint(main)

# Run the app
if __name__ == "__main__":
    if os.getenv("ENV") == "development":
        server = Server(app.wsgi_app)
        server.watch("app/**/*.py")
        server.watch("app/templates/**/*.html")
        server.watch("app/static/**/*.css")
        server.serve(port=5000)
    else:
        app.run(host="0.0.0.0", port=5000)
