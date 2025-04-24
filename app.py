from core import create_app, db
from flask_migrate import Migrate
from livereload import Server
from dotenv import load_dotenv
import os

load_dotenv(override=True)

# Detect environment
environment = os.getenv("ENV", "production")

# Create the Flask app using the factory
app = create_app(environment)

migrate = Migrate(app, db)

if __name__ == "__main__":
	# Use livereload for development environment
    if environment == "development":
        server = Server(app.wsgi_app)
        server.watch("app/**/*.py")
        server.watch("app/templates/**/*.html")
        server.watch("app/static/**/*.css")
        server.serve(port=5000)
    else:
        app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
