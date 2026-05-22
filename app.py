from flask import Flask
from config import DATABASE_URL
from extensions import db  # Import the neutral db instance

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Link the database instance to this running Flask app
db.init_app(app)

# Safely import models now that the circular loop is destroyed
from models.user import User
from models.activity import Activity

# Automatically create tables in Supabase
with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return "Database Connected and Tables Created Successfully!"

if __name__ == '__main__':
    app.run(debug=True)