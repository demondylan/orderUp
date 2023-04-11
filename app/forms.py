from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    DateField,
    TimeField,
    TextAreaField,
    BooleanField,
    SubmitField,
    PasswordField)
from wtforms.validators import DataRequired, ValidationError
from datetime import datetime

class LoginForm(FlaskForm):
    employee_number = StringField("Employee number", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Login")