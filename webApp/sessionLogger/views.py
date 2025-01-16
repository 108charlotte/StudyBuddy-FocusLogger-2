from django.shortcuts import render, redirect
from django.urls import path
import sqlite3

def home(request):
    return render(request, 'sessionLogger/index.html')  # Adjust the template path as needed

'''
# see README for how chatgpt was used in the creation of this code

# imports other than Flask and render_template are not my own code (see README)
from flask import Flask, flash, render_template, request, redirect, url_for, session
from flask_login import current_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3
import os

# Initialize the Flask application
app = Flask(__name__)

# chatgpt code snippet to fix secret_key not found error
app.secret_key = os.urandom(24)


@app.route("/")
def hello_world():
    return render_template("index.html", logged_in=current_user.is_authenticated)


# code from sitepoint article (see readme)
@app.route("/logout")
@login_required
def logout():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE user_id = ")
    return redirect(url_for("login"))


# this code is based off of the codeshack article I mentioned in my readme
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html", message="")

    if "username" in request.form:
        username = request.form["username"]
    else:
        return render_template("login.html", message="Please enter a username")

    if "password" in request.form:
        password = request.form["password"]
    else:
        return render_template("login.html", message="Please enter a password")

    password = generate_password_hash(password)

    # code originally from codeshack, copilot changed it from MySQL to sqlite3
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM users WHERE username = ?", (username, )
    )
    account = cursor.fetchone()

    if not account:
        flash("Invalid password")
        return render_template('login.html')
    
    stored_password_hash = account["password"]
    conn.close()

    if check_password_hash(stored_password_hash, password): 
        session["loggedin"] = True
        session["id"] = account["id"]
        session["username"] = account["username"]

        flash("Logged in successfully!")
        return redirect(url_for("index"))


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")

    username = request.form.get("username")
    password = request.form.get("password")
    password2 = request.form.get("password2")

    if password2 != password:
        flash("Passwords do not match")
        return render_template("register.html")

    if not (username and password):
        flash("Please fill out all fields")
        return render_template("register.html")

    hashed_password = generate_password_hash(password)

    # check if username already exists
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
    users = cursor.fetchone()

    if users:
        flash("This username is already taken")
        return render_template("register.html")

    cursor.execute(
        "INSERT INTO users (username, password) VALUES (?, ?)",
        (username, hashed_password),
    )

    flash("Registration successful")
    return render_template("login.html")


# Run the application
if __name__ == "__main__":
    app.run(debug=True)
'''
