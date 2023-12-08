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
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email=email, password=password).first()
        if user.role_id != 2:
            flash('You are not an user. Try login correctly.')
            return redirect(url_for('home'))
        return redirect(url_for('user_home'))

@app.route("/user_home", methods=["GET", "POST"])
def user_home():
    if request.method == "GET":
        return render_template('user_home.html')
    

@app.route("/user_signup", methods=["GET", "POST"])
def user_signup():
    if request.method == "GET":
        return render_template('user_signup.html')
    

@app.route("/admin_login", methods=["GET", "POST"])
def admin_login():
    if request.method == "GET":
        return render_template('admin_login.html')
    

@app.route("/creator", methods=["GET", "POST"])
def creator():
    if request.method == "Get":
        return render_template('creator.html')





