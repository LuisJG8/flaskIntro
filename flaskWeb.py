from flask import Flask, render_template
from flask_menu import Menu, register_menu


app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")


# @app.route("/user/<path:name>/")
# def who(name):
#     return f'hello {name}'


if __name__ == "__main__":
    app.run(debug=True)


# $env:FLASK_APP="base.py"
# then
#
# flask run