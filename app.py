from app import create_app, db
from flask_migrate import Migrate
from dotenv import load_dotenv
import os

load_dotenv(override=True)

app = create_app()
migrate = Migrate(app, db)

# Use Livereload only in development
if os.getenv("FLASK_ENV") == "development":
    from livereload import Server
    server = Server(app.wsgi_app)
    server.watch("app/**/*.py")
    server.watch("app/templates/**/*.html")
    server.watch("app/static/**/*.css")
    server.serve(port=5000)

