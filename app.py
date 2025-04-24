from app import create_app, db
from flask_migrate import Migrate
from livereload import Server
from dotenv import load_dotenv
import os

load_dotenv(override=True)

app = create_app()

migrate = Migrate(app, db)

# Dev server with live reload
if __name__ == "__main__":
    if os.getenv("FLASK_ENV") == "development":
        server = Server(app.wsgi_app)
        server.watch("app/**/*.py")
        server.watch("app/templates/**/*.html")
        server.watch("app/static/**/*.css")
        server.serve(port=5000)
    else:
        # app.run(host="0.0.0.0", port=int(os.getenv("PORT", 5000)))
        app.run(port=5000)
