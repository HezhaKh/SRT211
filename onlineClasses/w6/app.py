#!/usr/bin/env python3
from flask import Flask, request

app=Flask(__name__)

@app.route("/submit", methods=["POST"])
def submitForm():
    name=request.form["name"]
    lname=request.form["lastName"]
    addr=request.form["addr"]
    print(name)
    return  f"Form is submitted by {name} {lname} from {addr}"

if __name__=="__main__":
    app.run(debug=True,port=2024)