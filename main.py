from flask import Flask, render_template, url_for,  flash, redirect
# from forms import RegistrationForm, LoginForm
from email_validator import validate_email, EmailNotValidError

app = Flask(__name__,template_folder='templates', static_folder='static')

posts = [
    {
        'author': 'James Smith',
        'title': 'My Hackathon Journey',
        'content': 'I got to know about Major League Hacking when I was a first-year student',
        'date_posted': 'September 1st, 2021'
    },
    {
        'author': 'Jane Doe',
        'title': 'How I Ace My Interview',
        'content': 'You have to make sure to make an eye contact to the employees.',
        'date_posted': 'September 2nd, 2021'
    },
]

@app.route("/")
def home():
  return render_template("home.html", posts=posts)

@app.route("/signin")
def signin():
  return render_template("signin.html")


@app.route("/signup")
def signup():
  return render_template("signup.html")


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True, port=5000)
