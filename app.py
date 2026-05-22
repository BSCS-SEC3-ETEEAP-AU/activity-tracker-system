from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import DATABASE_URL

app = Flask(__name__)

# Bind the Supabase URI string to Flask-SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database engine
db = SQLAlchemy(app)

@app.route('/')
def home():
    return "Database Connected Successfully"

if __name__ == '__main__':
    app.run(debug=True)