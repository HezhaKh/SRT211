#!/usr/bin/env python3
"""
fileName: application.py
author: Hezha
dateAndTime: 3/20/24-11:40
description: to feed content of our website to the database
"""
from flask import Flask,request,render_template
import mysql # .connector

app =Flask(__name__)

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Password",
    database="flaskapp"
)

@app.route("/")
def form():
    return render_template('form.html')

@app.route("/submit",methods=['POST'])

def submit():
    name=request.form['name']
    email=request.form['email']
    cursor= db.cursor()
    cursor.execute("INSERT INTO users (name,email) values(%s,%s)",(name,email))
    db.commit()
    cursor.close()
    return 'Record has been submitted'
@app.route("/users")

def users():
    cursor =db.cursor(dictionary=True)
    cursor.execute("select * from users")
    users=cursor.fetchall()
    cursor.close()
    return render_template('users.html',users=users,title="Users page")

if __name__=='__main__':
    app.run()

