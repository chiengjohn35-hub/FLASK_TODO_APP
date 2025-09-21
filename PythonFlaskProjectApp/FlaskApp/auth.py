from flask import Blueprint, render_template, request, url_for, flash, session, redirect
from .forms import RegisterForm
from . import db
from .Models import User
from werkzeug.security import generate_password_hash, check_password_hash


auth = Blueprint("auth", __name__)


@auth.route("/register", methods=["POST", "GET"])
def register():
    if request.method=="POST":
        username = request.form.get("username")
        password = request.form.get("password")
        email = request.form.get("email")



        user = User.query.filter_by(username=username).first()

        if user:
            flash("Username Already Exists!", "info")
            return render_template("auth.signup")

        else:
            new_user = User(username=username, email=email ,password=generate_password_hash(password))
            db.session.add(new_user)
            db.session.commit()
            flash("Account Successfully Register!", "success")
            return redirect(url_for("auth.login"))


    return render_template("signup.html")

@auth.route("/login", methods=["POST","GET"])
def login():
    if request.method=="POST" :
        username = request.form.get('username')
        password = request.form.get("password")


        user = User.query.filter_by(username=username).first()
        check_hashed_password = check_password_hash(user.password, password)

        if user and check_hashed_password:
            session["username"]= username
            flash("Account Successfully Logged In!", "success")
            return redirect(url_for("main.course"))
        else:
            flash("Invalid Username or Password!")
            return render_template("login.html")

    return render_template("login.html")