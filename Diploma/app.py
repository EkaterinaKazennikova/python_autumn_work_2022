# init.py

from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# init SQLAlchemy so we can use it later in our models
db = SQLAlchemy()
migrate = Migrate()

login_manager = LoginManager()
login_manager.login_view = 'auth.login'


def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'katya_secret'
    app.config['TESTING'] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://postgres:4511@localhost:5432/kalk'

    db.init_app(app)

    with app.app_context():
        db.create_all()

    login_manager.init_app(app)
    return app

