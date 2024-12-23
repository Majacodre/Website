from flask import Flask, render_template, request
import pandas as pd
import json
import plotly
import plotly.express as px


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("main-page.html")

@app.route("/main-page.html")
def mainpage():
    return render_template ("main-page.html")

@app.route("/map.html")
def map():
    return render_template("map.html")

@app.route("/statistics.html")
def stats():
    return render_template("statistics.html")


