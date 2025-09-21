from flask_wtf import FlaskForm
from wtforms import PasswordField,StringField,SubmitField,EmailField
from wtforms.validators import input_required,Length, EqualTo


class RegisterForm(FlaskForm):
    username = StringField("Enter Username", validators=[input_required(), Length(min=5, max=10)])
    password = PasswordField("Enter Password", validators=[input_required(),
                                                           Length(min=7, max=12), EqualTo("confirm", message="Password Must Match")])
    confirm = PasswordField("Re-Enter Password", validators=[input_required(),
                                                           Length(min=7, max=12), EqualTo("password", message="Password Must Match")])
    email = EmailField("Email Address", validators=[input_required()])
    submit = SubmitField("REGISTER NOW")
    submit2 = SubmitField("LOGIN")