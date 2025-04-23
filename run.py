from app import create_app
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv(override=True)

# Detect environment (default to 'production' if not set)
environment = os.getenv("ENV", "production")

# Create the Flask app using the factory pattern
app = create_app()

if __name__ == "__main__":
    # Use livereload in development mode (optional)
    if environment == "development":
        from livereload import Server
        server = Server(app.wsgi_app)
        server.watch("app/**/*.py")
        server.watch("app/templates/**/*.html")
        server.watch("app/static/**/*.css")
        server.serve(port=5000)
    else:
        # Standard production server (for Railway, etc.)
        app.run(host="0.0.0.0", port=5000)
