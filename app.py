import sqlite3
from flask import Flask, redirect, render_template, request

app = Flask(__name__)

# connection = sqlite3.connect("users.db")

# cursor = connection.cursor()
# REWRITE
# cursor.execute(
#    "INSERT INTO users VALUES ('waxx567', 'waynem567@gmail.com', '99 Main St', 'Home Town', '6789', '+27791887713')")

CLIENT = "gaslitcatfish web designs"
CLIENT_1 = "gaslit"
CLIENT_2 = "catfish"
CLIENT_3 = "designs"
BUILDER = "fivefiftyfive ltd"
BUILDER_1 = "five"
BUILDER_2 = "fifty"
BUILDER_3 = "ltd"
YEAR = "2022"

# , CLIENT_1 = "gaslit", CLIENT_2 = "catfish", CLIENT_3 = "designs", BUILDER = "fivefiftyfive ltd", BUILDER_1 = "five", BUILDER_2 = "fifty", BUILDER_3 = "ltd", YEAR = "2022"}


@app.route("/")
def home():
    return render_template("index.html", site_info())


def input_to_lowercase(upper):
    for char in upper:
        return char.lower()


def site_info(CLIENT, etc):
    ...
    # returns inputs for app routes


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
