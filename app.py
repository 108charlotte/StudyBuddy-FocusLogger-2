# see README for how chatgpt was used in the creation of this code

# imports other than Flask and render_template are not my own code (see README)
from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
import MySQLdb.cursors
import MySQLdb.cursors, re, hashlib
from werkzeug.security import generate_password_hash

# Initialize the Flask application
app = Flask(__name__)
app.secret_key = "there_is_a_lopsided_octopus_somewhere_and_I_will_find_it"

# code snippet from codeshack article
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'pythonlogin'

mysql = MySQL(app)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login(): 
    return render_template('index.html', message='')

@app.route('/register', methods=['GET', 'POST'])
def register(): 
    if request.method == 'GET': 
        return render_template("register.html")
    username = request.form.get("username")
    password = request.form.get("password")
        
    if not (username and password): 
        return render_template("register.html", message="Please fill out all fields.")

    hashed_password = generate_password_hash(password)

    return redirect("/login")

# Run the application
if __name__ == '__main__':
    app.run(debug=True)

'''
<li><a href="/login">Login</a></li>
                    <li><a href="/register">Sign up</a></li>
                    {%else%}
                    <li><a href="/home">Login</a></li>
                    <li><a href="/setup_instructions">Extension Setup Instructions</a></li>
                    <li><a href="/extension_download">Extension Download</a></li>
'''