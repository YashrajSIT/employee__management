# importing Flask from flask
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Marshmallow # Import Flask-Migrate for database migrations
from .config import Config # Import the Config class from config.py
# Initialize SQLAlchemy and Marshmallow
db = SQLAlchemy()
ma = Marshmallow()

def create_app():
    app = Flask(__name__) # Create Flask application instance
    app.config.from_object(Config) 
    
    db.init_app(app)
    ma.init_app(app)
  # Initialize Marshmallow with the Flask app
    from .routes import routes
    app.register_blueprint(routes)
 # Import and register main routes blueprint
    from .errors import errors
    app.register_blueprint(errors)

    return app