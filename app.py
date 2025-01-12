# see README for how chatgpt was used in the creation of this code

# imports other than Flask and render_template are not my own code (see README)
from flask import Flask, flash, render_template, request, redirect, url_for, session
from flask_login import current_user, login_required
from werkzeug.security import generate_password_hash
import sqlite3

# Initialize the Flask application
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html', logged_in=current_user.is_authenticated)

# code from sitepoint article (see readme)
@app.route('/logout')
@login_required
def logout(): 
    logout_user()
    return redirect(url_for('login'))

# this code is based off of the codeshack article I mentioned in my readme
@app.route('/login', methods=['GET', 'POST'])
def login(): 
    if request.method == 'GET':
        return render_template('login.html', message='')
    
    if 'username' in request.form: 
        username = request.form['username']
    else: 
        return render_template('login.html', message='Please enter a username')
    
    if 'password' in request.form: 
        password = request.form['password']
    else: 
        return render_template('login.html', message='Please enter a password')
    
    password = generate_password_hash(password)

    # code originally from codeshack, copilot changed it from MySQL to sqlite3
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password))
    account = cursor.fetchone()

    if account: 
        session['loggedin'] = True
        session['id'] = account['id']
        session['username'] = account['username']

        flash('Logged in successfully!')
        return redirect(url_for('index'))
    
    return render_template('login.html', message='Incorrect username or password')
    


@app.route('/register', methods=['GET', 'POST'])
def register(): 
    if request.method == 'GET': 
        return render_template("register.html")
    
    username = request.form.get("username")
    password = request.form.get("password")
        
    if not (username and password): 
        return render_template("register.html", message="Please fill out all fields.")

    hashed_password = generate_password_hash(password)

    return redirect("/login", message="Registered successfully")


# Run the application
if __name__ == '__main__':
    app.run(debug=True)