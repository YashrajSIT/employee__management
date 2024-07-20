# importing flask from flask
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from model import db   
from model import Employee
from routes import main_blueprint # Import the main blueprint from routes.py
from config  import   Config #Import the Config class from config.py
# Initialize Flask app
app = Flask(__name__)

app.config.from_object('config.Config')
db = SQLAlchemy(app)

from routes import *
# Run the Flask application if executed directly
if __name__ == '__main__':
    app.run(debug=True)