#!/usr/bin/env python3
from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/comparisons")
def comparisons():
    return render_template("comparisons.html")

@app.route('/chaoyang')
def maxTemp():
    return render_template('chaoyang.html')

@app.route('/haidian')
def humidity():
    return render_template('haidian.html')

@app.route('/xicheng')
def cloudiness():
    return render_template('xicheng.html')

@app.route('/dongcheng')
def windspeed():
    return render_template('dongcheng.html')

@app.route('/data')
def data():
    return render_template('data.html')

if __name__ == "__main__":
    app.run(debug=True)
