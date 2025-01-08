import os

from flask import Flask, render_template, request
from mapgen import mapgen


basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

@app.route("/")
def index():
    m = mapgen()
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')