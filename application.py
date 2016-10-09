from flask import Flask
from flask import render_template
from flask import request, flash
app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    """
    display the index page of the portfolio
    """
    if request.method == 'POST':
        print(str(request.form['emailInput']))
        return render_template('index.html')
    else:
        return render_template('index.html')

@app.errorhandler(404)
def page_not_found(error):
    """
    Redirect to the index page if someone is accessing a non-existant route
    """
    return render_template('index.html'), 404
