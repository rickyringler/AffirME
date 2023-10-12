from flask import Flask, render_template, url_for, request, redirect, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime as dt
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
@app.route("/")
def home():
    return render_template("home.html",
                           title="Home")
@app.route("/todaysaffirmation")
def affirmation():
    return render_template("todays_affirmations",
                           title="TodaysAffirmation")
@app.route("/philosophyquote")
def quote():
    return render_template("philosophy_quotes.html",
                           title="TodaysPhilosophyQuote")
@app.route("/yogapose")
def yoga():
    return render_template("yoga_poses.html",
                           title="TodaysYogaPose")

if __name__=="__main__":
    app.run(debug=True)
