import sqlite3
from flask import Flask, redirect, render_template, request

connection = sqlite3.connect("users.db")

cursor = connection.cursor()
cursor.execute(
    "INSERT INTO users VALUES ('waxx567', 'waynem567@gmail.com', '99 Main St', 'Home Town', '6789', '+27791887713')")

# FORGOT THE USER'S ACTUAL NAME/S
# DELETE ALL FROM OLD TABLE EXCEPT

# user - user-id, user-name

# names - name-id, user-id, name
# address - address-id, name-id, street, city, state, postcode, country
# phone - phone-id, name-id, phone-number

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
