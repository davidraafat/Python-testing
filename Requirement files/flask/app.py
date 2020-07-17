from flask import Flask, request, render_template

app = Flask(__name__, static_folder='assets')


# Retrun a string
@app.route("/")
def hello_world():
    return render_template('index.html')

# Process form data
@app.route("/login", methods=['POST'])
def login():
    return "<h2>Hello " + request.form['username']+('</h2><br>'+
    '<button id="logout" onclick="window.location.href='+"'/'"+'">Log out</button>')
