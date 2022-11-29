from flask import Flask
from flask import request, render_template
from flask_sqlalchemy import SQLAlchemy
import bcrypt
import re


app = Flask(__name__)
db = SQLAlchemy()
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://postgres:4511@localhost:5432'
db.init_app(app)

class Account(db.Model):
    __tablename__ = "account"
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String)
    password = db.Column(db.String)
    email = db.Column(db.String)
    parameters = db.relationship('parameters', backref='account')

class Parameters(db.Model):
    __tablename__ = "parameters"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String, nullable=False)
    weight = db.Column(db.Integer, nullable=False)
    height = db.Column(db.Integer, nullable=False)

class Nutrition(db.Model):
    __tablename__ = "nutrition"
    id = db.Column(db.Integer, primary_key=True)
    food = db.Column(db.Integer, unique=True, nullable=False)
    water = db.Column(db.Integer, nullable=False)
    workout = db.Column(db.Integer, nullable=False)

with app.app_context():
    db.create_all()

'''Валидация формата пароля'''
class ValidationError(Exception):
    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z\d]{8,}$'
    def validate_by_regexp(password, pattern):
        if re.match(pattern, password) is None:
            raise ValidationError('Введите пароль,содержащий не менее 8 символов в обоих регистрах')

@app.route("/")
def Head():
    return render_template("index.html", title= "Healthy Nutrition")


@app.route("/account/create", methods=["GET", "POST"])
def account_create():
    if request.method == "POST":
        hashAndSalt = bcrypt.hashpw(request.form["password"].encode(), bcrypt.gensalt())
        account = Account(
            login=request.form["login"],
            password=hashAndSalt,
            email=request.form["email"],
        )
        db.session.add(account)
        db.session.commit()
        return "Вы успешно зарегистрированы"
        return redirect(url_for("parameters_detail", id=parameters.id))

    return render_template("account.html")

@app.route("/parameters/create", methods=["GET", "POST"])
def parameters_create():
    if request.method == "POST":
        parameters = Parameters(
            username = request.form["username"],
            age = request.form["age"],
            gender = request.form["gender"],
            weight = request.form["weight"],
            height = request.form["height"]
        )
        db.session.add(parameters)
        db.session.commit()
        if gender == 'male':
            return "Ваша дневная норма каллорий", lambda weight,height,age: 88 + weight * 14 + height * 5 - 6 * age
        else:
            return "Ваша дневная норма каллорий", lambda weight,height,age: 447 + weight * 9 + height * 3 - 4 * age
        return redirect(url_for("parameters_detail", id=parameters.id))

    return render_template("parameters.html")

@app.route("/nutrition/create", methods=["GET", "POST"])
def nutrition_create():
    if request.method == "POST":
        nutrition = Nutrition(
            food = request.form["food"],
            water = request.form["water"],
            workout = request.form["workout"],
        )
        db.session.add(nutrition)
        db.session.commit()
        return "Вы успешно внесли свои данные"
        return redirect(url_for("nutrition_detail", id=nutrition.id))

    return render_template("nutrition.html")




if __name__ == "__main__":
    app.run()