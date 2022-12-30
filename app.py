import sqlite3
from flask import Flask, redirect, render_template, request

connection = sqlite3.connect("users.db")

cursor = connection.cursor()


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
