from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, validators
from wtforms.validators import DataRequired, Length, Email, EqualTo

class RegistrationForm(FlaskForm): #DataRequired = can't be null
  username = StringField('Username', validators=[DataRequired(), validators.Length(min=5, max=20)])
  email = StringField('Email', validators=[DataRequired(), Email()])
  password = PasswordField('Password', validators=[DataRequired()])
  confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
  submit = SubmitField('Sign Up')

class LoginForm:
  username = StringField("Username", validators = [DataRequired(), validators.Length(min=5, max = 20)])
  password = StringField("Password", validators = [DataRequired()])
  