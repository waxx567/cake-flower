import sqlite3
from flask import Flask, redirect, render_template, request

app = Flask(__name__)

# Connect to database
conn = sqlite3.connect("users.db")

# Create a cursor
c = conn.cursor()

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
    return render_template("index.html")


def input_to_lowercase(upper):
    for char in upper:
        return char.lower()


def site_info(CLIENT, etc):
    ...
    # returns inputs for app routes
