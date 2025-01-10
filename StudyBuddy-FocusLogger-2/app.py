# this is CHATGPT starter code for creating a basic flask application

from flask import Flask, render_template

# Initialize the Flask application
app = Flask(__name__)

# Define a basic route
@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login(): 
    return render_template('home.html')


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