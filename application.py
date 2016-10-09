from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
def index():
    """
    display the index page of the portfolio
    """
    return render_template('index.html')

@app.errorhandler(404)
def page_not_found(error):
    """
    Redirect to the index page if someone is accessing a non-existant route
    """
    return render_template('index.html'), 404
