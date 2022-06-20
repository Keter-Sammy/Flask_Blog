import posts as posts
from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
from flask_sqlalchemy import SQLAlchemy
from models import User, Post


app = Flask(__name__)
app.config["SECRET_KEY"] = "4dedadae485e559b5db72a57767187b5"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class User(db.Model):


    posts = [
    {
        "author": "Keter",
        "title": "Blog 1",
        "content": "First Post Content",
        "date_posted" : " May 10th 2022"
    },
{
        "author": "Sammy",
        "title": "Blog 2",
        "content": "Second Post Content",
        "date_posted" : " May 11th 2022"
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", posts=posts)

@app.route("/about")
def about():
    return render_template("about.html", title="About")


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f"Account Created for {form.username.data}!", "success")
        return redirect(url_for("home"))
    return render_template("register.html", title="Register", form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == "admin@blog.com" and form.password.data == "password":
            flash("Login Successful!", "success")
            return redirect(url_for("home"))
        else:
            flash("Login Failed. Check Username and Password", "danger")
    return render_template("login.html", title="Login", form=form)


if __name__ == "__main__":
    app.run(debug=True)