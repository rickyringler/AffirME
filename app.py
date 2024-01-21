#Ricky Ringler : AffirME
#Repo : https://github.com/rickyringler/AffirME
#Documentation : https://github.com/rickyringler/AffirME/blob/master/README.md

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

'''
MIT License

Copyright (c) [Year] [Your Name]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''
