#Documentation:
#Chart.js documentation: https://www.chartjs.org/docs/latest/
#clearing ad updating graph in chart.js: https://www.chartjs.org/docs/latest/developers/updates.html
#localStorage in js: https://code-maven.com/slides/javascript/local-storage-boolean
#innerHTML updating: https://www.w3schools.com/js/js_htmldom_events.asp
#setInterval for website to automatically call websocket: https://www.w3schools.com/jsref/met_win_setinterval.asp

from flask import Flask, render_template, request, jsonify
import requests
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap
import urllib.request, json
from datetime import datetime


app = Flask(__name__)
app.secret_key = "super secret"
bootstrap = Bootstrap(app)


@app.route('/')
def home():
    return render_template("home.html")


@app.route("/trends")
def trends():
    return render_template("trends.html")


@app.route("/test")
def test():
    return render_template("testing.html")


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")


if __name__ == '__main__':
    app.run()
