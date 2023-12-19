from flask import request, redirect, url_for, flash, session
from flask import render_template
from flask import current_app as app
from application.models import *
from .database import db

@app.route("/", methods=["GET"])
def home():
    return render_template("home.html")
       
@app.route("/user_login", methods=["GET", "POST"])
def user_login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email=email, password=password).first()
        if not user:
            flash("Incorrect credentials")
            return redirect(url_for('user_login'))
        if user.role_id != 2:
            flash('You are not an user. Try login correctly.')
            return redirect(url_for('home'))
        session["email"] = email
        return redirect(url_for('user_home'))
    return render_template("access.html",login=True)

@app.route("/user_signup", methods=["GET", "POST"])
def user_signup():
    if request.method == "POST":
        email = request.form['email']
        name = request.form['name']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        if password != confirm_password:
            flash('Password not matched')
            return redirect(url_for('user_signup'))
        user = User(email=email, name=name, password=password)
        db.session.add(user)
        db.session.commit()
        flash('Signed up successful')
        return redirect(url_for('user_login'))
    return render_template('access.html',login=False)

@app.route("/admin_login", methods=["GET", "POST"])
def admin_login():
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email=email, password=password).first()
        if not user:
            flash("Incorrect credentials")
            return redirect(url_for('admin_login'))
        if user.role_id != 1:
            flash('You are not an admin. Try login correctly.')
            return redirect(url_for('home'))
        return redirect(url_for('admin_home'))
    return render_template('access.html',admin=True)
    
@app.route("/user_home", methods=["GET"])
def user_home():
    user = User.query.filter_by(email = session['email']).first()
    if user is not None:
        songs = Song.query.all()
        return render_template('user_home.html', username = user.name, songs = songs, title=str.title)
    else:
        return redirect("/")
    
@app.route("/admin_home", methods=["GET"])
def admin_home():
    users = User.query.filter_by(creator = 0).all()
    creators = User.query.filter_by(creator = 1).all()
    return render_template('admin_home.html', users=users, creators=creators, len=len)


@app.route("/creator", methods=["GET", "POST"])
def creator():
    if session["email"] is not None:
        user = User.query.filter_by(email = session['email']).first()
        if user.creator ==  False:
            return render_template("creator_home.html")
        else:
            return render_template("creator_dashboard2.html", username = user.name)
    else:
        return redirect("/")

@app.route("/registerAsCreator", methods=["GET", "POST"])
def registerAsCreator():
    if session["email"] is not None:
        user = User.query.filter_by(email = session['email']).first()
        user.creator = True
        db.session.commit()
        return redirect(url_for("creator"))
    else:
        return redirect("/")

@app.route("/logout")
def logout():
    if session["email"] is not None:
        session.pop("email", None)
        return redirect("/")
    else:
        return redirect("/")



