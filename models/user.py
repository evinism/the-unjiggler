from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)


class User(db.Model):
  __tablename__ = "users"
  id = db.Column(db.Integer, primary_key=True)
  first_name = db.Column(db.Text, unique=False, nullable=False)
  last_name = db.Column(db.Text, unique=False, nullable=False)
  email = db.Column(db.Text, unique=True, nullable=False)
  active = db.Column(db.Boolean, default=False)
  tokens = db.Column(db.Text)
  created_at = db.Column(db.DateTime, default=datetime.utcnow())
  updated_at = db.Column(db.DateTime, default=datetime.utcnow())

def __init__(self, first_name, last_name, email):
  self.first_name = first_name
  self.last_name = last_name
  self.email = email

def __repr__(self):
  return '<User %r>' % self.email
