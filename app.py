import sqlite3
from flask import Flask, redirect, render_template, request

connection = sqlite3.connect("users.db")

cursor = connection.cursor()
cursor.execute(
    "INSERT INTO users VALUES ('waxx567', 'waynem567@gmail.com', '4 Shaw St', 'Shit Towne', '6789', '+27791887713')")

    # FORGOT THE USER'S ACTUAL NAME/S 

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
