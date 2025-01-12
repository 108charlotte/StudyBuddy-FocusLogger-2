# see README for how chatgpt was used in the creation of this code

# imports other than Flask and render_template are not my own code (see README)
from flask import Flask, flash, render_template, request, redirect, url_for, session
from flask_login import current_user, login_required
from werkzeug.security import generate_password_hash
import sqlite3

# Initialize the Flask application
app = Flask(__name__)

# code snippet altered from medium article
def create_users_database(): 
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE users (username TEXT, password TEXT, user_id INTEGER PRIMARY KEY AUTOINCREMENT)''')
    conn.commit()
    conn.close()

def create_session_database(): 
    conn = sqlite3.connect('sessions.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE sessions (session_id TEXT PRIMARY KEY AUTOINCREMENT, user_id INTEGER, goal TEXT, duration TEXT, start_time TEXT)''')
    conn.commit()
    conn.close()

@app.route('/')
def hello_world():
    return render_template('index.html')

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
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password))
    account = cursor.fetchone()

    if account: 
        session['loggedin'] = True
        session['id'] = account['id']
        session['username'] = account['username']

        flash('Logged in successfully!')
        return redirect(url_for('index'))
    


@app.route('/register', methods=['GET', 'POST'])
def register(): 
    if request.method == 'GET': 
        return render_template("register.html")
    username = request.form.get("username")
    password = request.form.get("password")
        
    if not (username and password): 
        return render_template("register.html", message="Please fill out all fields.")

    hashed_password = generate_password_hash(password)

    message = ""
    return redirect("/login", msg=message)


# Run the application
if __name__ == '__main__':
    app.run(debug=True)