from flask_sqlalchemy import SQLAlchemy

# This sits in a neutral zone, preventing files from looping back to app.py
db = SQLAlchemy()