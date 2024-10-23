import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)

def create_app():
    app = Flask(__name__)
    app.secret_key = os.environ.get("FLASK_SECRET_KEY") or "a_secure_secret_key"

    # Use PostgreSQL database URL from environment variable
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
    if app.config["SQLALCHEMY_DATABASE_URI"] and app.config["SQLALCHEMY_DATABASE_URI"].startswith("postgres://"):
        app.config["SQLALCHEMY_DATABASE_URI"] = app.config["SQLALCHEMY_DATABASE_URI"].replace("postgres://", "postgresql://", 1)

    app.config["SQLALCHEMY_ENGINE_OPTIONS"] = {
        "pool_recycle": 300,
        "pool_pre_ping": True,
    }

    db.init_app(app)

    with app.app_context():
        import models
        db.create_all()

<<<<<<< HEAD
    # Import routes after creating the app
    from routes import index, services, about, contact, landing_page, thank_you, download_ebook

    # Register the routes
    app.add_url_rule('/', 'index', index)
    app.add_url_rule('/services', 'services', services)
    app.add_url_rule('/about', 'about', about)
    app.add_url_rule('/contact', 'contact', contact, methods=['GET', 'POST'])
    app.add_url_rule('/landing', 'landing_page', landing_page, methods=['GET', 'POST'])
    app.add_url_rule('/thank-you', 'thank_you', thank_you)
    app.add_url_rule('/download-ebook', 'download_ebook', download_ebook, methods=['POST'])
=======
    # Import routes after initializing the app and db
    from routes import *
>>>>>>> origin/main

    return app

app = create_app()

<<<<<<< HEAD
=======
# Vercel serverless function handler
def handler(event, context):
    return app.wsgi_app

>>>>>>> origin/main
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
