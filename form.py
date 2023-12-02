from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class RegistrationForm(FlaskForm):
    first_name = StringField('First Name',
                           validators=[DataRequired(), Length(min=2, max=20)])
    last_name = StringField('Last Name',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                           validators=[DataRequired(), Email()])
    password = PasswordField('Pasword',
                           validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Pasword',
                           validators=[DataRequired(), EqualTo(password)])
    submit = SubmitField('Register')


class LoginForm(FlaskForm):
    email = StringField('Email',
                           validators=[DataRequired(), Email()])
    password = PasswordField('Pasword',
                           validators=[DataRequired()])
    remember = BooleanField('Remembe me')
    submit = SubmitField('Log in')
    