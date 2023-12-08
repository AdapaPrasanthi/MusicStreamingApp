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
        return render_template('user_home.html')





