from flask import Flask, render_template, url_for, flash, redirect, request, session
from forms import RegistrationForm, LoginForm, Post
from email_validator import validate_email, EmailNotValidError
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
import os

client_id = os.environ['client_id']
client_secret = os.environ['client_secret']

cloud_config= {
  'secure_connect_bundle': 'secure-connect-letsshill.zip'
}
auth_provider = PlainTextAuthProvider(client_id, client_secret)
cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
session2 = cluster.connect()

app = Flask(__name__,template_folder='templates', static_folder='static')

app.config['SECRET_KEY'] = "8b6dd776fdab11e0a2e60f8b0f284bc3"
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

@app.route("/", methods = ['GET', 'POST'])
def home():
  form = Post(request.form)
  text = form.postf.data
  if 'username' in session:
    username = session['username']
    print(username)
    if request.method == "POST" and form.validate_on_submit:
      row = session2.execute("insert into ls.posts (username, post, url) values ('"+username+"', '"+text+"', 'https://google.com')")
      if row:
        flash("posted!", "success")
  return render_template("home.html", posts=posts)

@app.route("/signin", methods=['GET', 'POST'])
def signin():
  form = LoginForm(request.form)
  username = form.username.data
  password = form.password.data
  print(username)
  print(password)
  if request.method == "POST" and form.validate_on_submit:
    row = session2.execute("select username, password, email from ls.accounts where username = '"+username+"' and password ='"+password+"' ALLOW FILTERING;").one()
    print(row)
    email = row[2]
    print(email)
    if row:
      flash('You have successfully logged in.', "success")
      session['logged_in'] = True
      session['email'] = email
      session['username'] = username
  return render_template("signin.html")


@app.route("/signup", methods=['GET', 'POST'])
def signup():
  form = RegistrationForm(request.form)
  username = form.username.data
  password = form.password.data
  email = form.email.data
  if form.validate_on_submit and request.method == "POST":
    row = session2.execute("insert into ls.accounts(username, email, password) values ('"+username+"', '"+email+"', '"+password+"')")
    print(row)
    flash('Your account is created successfully!', 'success')
    # return redirect(url_for('home'))
  return render_template("signup.html", form = form)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True, port=5000)
