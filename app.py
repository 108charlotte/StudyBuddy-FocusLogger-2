# see README for how chatgpt was used in the creation of this code

# imports other than Flask and render_template are not my own code (see README)
from flask import Flask, flash, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
from flask_login import current_user, login_required
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
    
    hash = password + app.secret_key
    hash = hashlib.sha1(hash.encode())
    password = hash.hexdigest()

    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT * FROM accounts WHERE username = %s AND password = %s', (username, password))
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