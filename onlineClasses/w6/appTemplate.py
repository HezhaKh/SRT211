#!/usr/bin/env python3
from flask import Flask, jsonify, render_template
import flask_cors

app=Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def aboutUs():
    return render_template("aboutUs.html")

if __name__=="__main__":
    app.run(debug=True,port=2034)