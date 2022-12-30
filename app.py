from flask import Flask, redirect, render_template, request, session, url_for, flash
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
