from flask import Flask, render_template
from task_scheduler import *
app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html",
                           title="Home")
@app.route("/todaysaffirmation")
def affirmation():
    return render_template("todays_affirmation.html",
                           title="TodaysAffirmation", data=temp_affirmation)

@app.route("/philosophyquote")
def quote():
    return render_template("philosophy_quotes.html",
                           title="TodaysPhilosophyQuote", data=temp_quote)
@app.route("/yogapose")
def yoga():
    return render_template("yoga_poses.html",
                           title="TodaysYogaPose", data=temp_pose)

if __name__=="__main__":
    app.run(debug=True)
