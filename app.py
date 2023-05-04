from flask import Flask, Blueprint, g, render_template, request, redirect, url_for, session, jsonify, flash, escape
from flask_bootstrap import Bootstrap
from werkzeug.security import generate_password_hash, check_password_hash
from simayiAPI.sqlAPI import DB
from error_pages import error_pages
from user_pages import user_pages
from election_pages import election_pages
from simayiAPI.BlockchainKeyGenerator import BlockchainKeyGenerator
import hashlib

# Codes for initialising the flask application
app = Flask(__name__)
app.register_blueprint(error_pages)
app.register_blueprint(user_pages)
app.register_blueprint(election_pages)
app.config['USE_SESSION_FOR_NEXT'] = True

# Code for using flask-bootstrap
bootstrap = Bootstrap(app) 
        
"""
HTTP status code 400 is given when there is a bug while running the app locally.
To check the cause of the bug, 
1. Make bad_request + page400 functions have been commented(?)
2. Make sure you are running the app in debug mode (it is currently executed in debug mode though)
"""
@app.errorhandler(400)
def bad_request(e):
    return render_template('error/400.html'), 400

#HTTP status code 404 is given when there is no such page for the given URL.
@app.errorhandler(404)
def page_not_found(e):
    return render_template('error/404.html'), 404
    
@app.errorhandler(408)
def request_timeout(e):
    return render_template('error/408.html'), 408

@app.errorhandler(410)
def gone(e):
    return render_template('error/410.html'), 410

@app.errorhandler(429)
def too_many_requests(e):
    return render_template('error/429.html'), 429

@app.errorhandler(431)
def request_header_fields_too_large(e):
    return render_template('error/431.html'), 431

@app.errorhandler(451)
def unavailable_for_legal_reasons(e):
    return render_template('error/451.html'), 451

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('error/500.html'), 500

@app.errorhandler(503)
def service_unavailable(e):
    return render_template('error/503.html'), 503

@app.route('/', methods = ['GET'])
@app.route('/home', methods = ['GET'])
def home():
    if request.method == 'GET':
        return render_template('home.html')

@app.route('/about', methods = ['GET'])
def about():
    if request.method == 'GET':
        return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)