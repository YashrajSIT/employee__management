# importing os

import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///employees.db'  # SQLite database URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Disable modification tracking for SQLAlchemy
    SECRET_KEY = os.urandom(24)  # Generate a random secret key for security