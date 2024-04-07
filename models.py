"""Models for Blogly."""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)


class User(db.Model):
    """User"""

    __tablename__ = "Users"

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    first_name = db.Column(db.String(30),
                     nullable=False,
                     unique=True)
    last_name = db.Column(db.String(30),
                     nullable=False,
                     unique=True)
    image_url = db.Column(db.Text,
                     nullable=True,
                     default="https://paradisevalleychristian.org/wp-content/uploads/2017/01/Blank-Profile.png")
    