from app import create_app, db  # Import create_app  and db from app 

app = create_app() # Create the Flask application using the create_app function
# Checking if the script is being run directly or not
if __name__ == '__main__':
    # Run the Flask application in debug mode if true
    app.run(debug=True)