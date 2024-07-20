from app import create_app, db #mport create_app and db  from app 
# Create the Flask application using the create_app function
app = create_app()

with app.app_context():
    db.create_all()
    print("Database initialized!") #printing message