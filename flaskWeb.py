from flask import Flask, render_template
from flask_menu import Menu, register_menu
import requests






app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")


@app.route('/<name>')
def user(name):
    connection = requests.get(f"https://api.genderize.io?name={name}").json()
    print(connection)
    name = connection["name"]
    gender = connection["gender"]
    print(name, gender)

    connection_two = requests.get(f"https://api.agify.io?name={name}").json()
    print(connection_two)
    name_two = connection_two["name"]
    age = connection_two["age"]
    print(name_two, age)

    return render_template("index.html", name=name, gender=gender, age=age)


# @app.route("/user/<path:name>/")
# def who(name):
#     return f'hello {name}'


if __name__ == "__main__":
    app.run(debug=True)


# $env:FLASK_APP="base.py"
# then
#
# flask run