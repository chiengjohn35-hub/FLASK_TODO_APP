from flask import Blueprint, render_template
from .forms import RegisterForm


main = Blueprint("main", __name__)


@main.route("/")
def home():
    return render_template("base.html")

@main.route("/")
def course():
    form = RegisterForm()
    return render_template("course.html", form=form)

