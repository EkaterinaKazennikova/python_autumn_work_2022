from flask import Flask
from flask_sqlalchemy import SQLAlchemy

#create the extension
db = SQLAlchemy()
# create the app
app = Flask(__name__)
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://postgres:4511@localhost:5432'
db.init_app(app)

class Filter(db.Model):
    __tablename__ = "filter"
    id = db.Column(db.Integer, primary_key=True)
    country = db.Column(db.String, unique=True, nullable=False)
    city = db.Column(db.String)
    duration = db.Column(db.Integer, nullable=False)
    nutrition = db.Column(db.String, unique=True, nullable=False)
    hotel = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    id_customers = db.Column(db.ForeignKey('customers.id'))

class Customers(db.Model):
    __tablename__ = "customers"
    id = db.Column(db.Integer, primary_key=True)
    surname = db.Column(db.String)
    age = db.Column(db.Integer, nullable=False)
    discount = db.Column(db.Boolean, nullable=True)
    filter = db.relationship('filter', backref='customers')
    id_workers = db.Column(db.ForeignKey('workers.id'))

class Workers(db.Model):
    __tablename__ = "workers"
    id = db.Column(db.Integer, primary_key=True)
    surname = db.Column(db.String)
    customers = db.relationship('customers', backref='workers')

with app.app_context():
  db.create_all()