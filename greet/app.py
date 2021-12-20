from flask import Flask, request

app = Flask(__name__)

@app.route('/welcome')
def welcome():
    return "weclome"

@app.route('/welcome/back')
def welcome_back():
    return "weclome back"

@app.route('/welcome/home')
def welcome_home():
    return "weclome home"



