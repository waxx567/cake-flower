import csv

from cs50 import SQL

db = SQL("sqlite:///users.db")

username = input("Username: ").strip()
email = input("Email: ")

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
