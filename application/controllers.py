from flask import request, redirect, url_for, flash
from flask import render_template
from flask import current_app as app
from application.models import *
from .database import db

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == 'GET':
        return render_template("home.html")

       
@app.route("/user_login", methods=["GET", "POST"])
def user_login():
    if request.method == 'GET':
        return render_template("user_login.html")
    elif request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        print(username, password)
        user = User.query.filter_by(name=username, password=password)
        print(user)





