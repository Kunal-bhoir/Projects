from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return 'Home Page'
    
@app.route('/about')
def About():
    return 'About Page'