from flask import Flask, Blueprint, g, render_template, request, redirect, url_for, session, jsonify, flash, escape
from flask_bootstrap import Bootstrap
from werkzeug.security import generate_password_hash, check_password_hash
from simayiAPI.sqlAPI import DB
from error_pages import error_pages
from my_pages import my_pages
from voting_pages import voting_pages # Perhaps not needed.
from election_pages import election_pages
from simayiAPI.BlockchainKeyGenerator import BlockchainKeyGenerator
import hashlib

# Codes for initialising the flask application
app = Flask(__name__)
app.register_blueprint(error_pages)
app.register_blueprint(my_pages)
app.register_blueprint(voting_pages)
app.register_blueprint(election_pages)
app.secret_key = "PinguPenguinPingu".encode('utf8')
app.config['USE_SESSION_FOR_NEXT'] = True

# Code for using flask-bootstrap
bootstrap = Bootstrap(app) 

"""
function before_request is executed before the first request is made.
There is a separate function called teardown_request which is executed once every request has been completed.
Since teardown_request is not needed for this application, I have not created.
e.g. if teardown_request is used to disconnect the database, every time the client has finished its request,
the database will be disconnected and therefore have to reconnect the database whenever he or she makes a new request.

g is a global variable for flask. Hence I have used the variable 
1. g.db to maintain the connection til the client closes the web applicaiton,
2. g.userName to store the userName and thereby not use try except method to check the userName for each page
"""

@app.before_request
def before_request():
    if 'db' not in g:
        g.db = DB()
    else:
        g.db.connectDB()
    if 'userName' in session:
        g.userName = str(escape(session['userName']))
    else:
        g.userName = None
        
"""
HTTP status code 400 is given when there is a bug while running the app locally.
To check the cause of the bug, 
1. Make bad_request + page400 functions have been commented(?)
2. Make sure you are running the app in debug mode (it is currently executed in debug mode though)
"""
@app.errorhandler(400)
def bad_request(e):
    return render_template('error/400.html', userName = g.userName), 400

#HTTP status code 404 is given when there is no such page for the given URL.
@app.errorhandler(404)
def page_not_found(e):
    return render_template('error/404.html', userName = g.userName), 404
    
@app.errorhandler(408)
def request_timeout(e):
    return render_template('error/408.html', userName = g.userName), 408

@app.errorhandler(410)
def gone(e):
    return render_template('error/410.html', userName = g.userName), 410

@app.errorhandler(429)
def too_many_requests(e):
    return render_template('error/429.html', userName = g.userName), 429

@app.errorhandler(431)
def request_header_fields_too_large(e):
    return render_template('error/431.html', userName = g.userName), 431

@app.errorhandler(451)
def unavailable_for_legal_reasons(e):
    return render_template('error/451.html', userName = g.userName), 451

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('error/500.html', userName = g.userName), 500

@app.errorhandler(503)
def service_unavailable(e):
    return render_template('error/503.html', userName = g.userName), 503

@app.route('/', methods = ['GET'])
@app.route('/home', methods = ['GET'])
def home():
    if request.method == 'GET':
        return render_template('home.html', userName = g.userName)

@app.route('/signout')
def signout():
    session.pop('userName', None)
    g.db.disconnectDB() # Remove the connection with the database as there is no need after signing out
    return redirect(url_for('home'))

@app.route('/signup', methods =['GET', 'POST'])
def signup():
    if request.method == 'GET':
         return render_template('signup.html', userName = g.userName)
     
    if request.method == 'POST':
        userName = request.form.get('userName')
        fullName = request.form.get('fullName')
        password = request.form.get('password')
        confirmPassword = request.form.get('confirmpassword')
        email = request.form.get('email')
        
        encryptedPassword = generate_password_hash(password)
        
        if not userName or not fullName or not password or not confirmPassword or not email:
            msg = 'Please fill out the form!'
            flash(msg)
            return redirect(url_for('signup')) 
        elif password != confirmPassword:
            msg = 'Please confirm your password again.'
            flash(msg)
            return redirect(url_for('signup')) 
        else:
            accountExistence = g.db.getUserNameExistence(userName)[0]

            # Case: There is already an account with same userName
            if accountExistence == 1:
                msg = "The account with username as " + str(userName) + " already exists!"
                flash(msg)
                return redirect(url_for('signup')) 
            # Case: the form has been filled out
            else:
                # userID = hashed userName
                userID = hashlib.sha256(userName.encode()).hexdigest()
                keyGenerator = BlockchainKeyGenerator()
                publicKey, privateKey = keyGenerator.generate_keys()
                g.db.addUser(userID, userName, encryptedPassword, fullName, email, publicKey, privateKey)
                msg = 'You have successfully registered your account!'
                flash(msg)
                session['userName'] = userName
                g.userName = userName
                return redirect(url_for('home'))
           
@app.route('/signin', methods =['GET', 'POST'])
def signin():
    if request.method == 'GET':
        return render_template('signin.html', userName = g.userName)
    if request.method == 'POST':
        userName = request.form.get('userName')
        password = request.form.get('password')
        if not userName or not password:
            msg = "Please fill out the form!"
            flash(msg)
            return redirect(url_for('signin'))
        
        accountExistence = g.db.getUserNameExistence(userName)[0]
        if accountExistence == 0:
            msg = "There is no such account created with the username - " + str(userName) + "."
            flash(msg)
            return redirect(url_for('signin')) 
        
        accountName, accountPassword = g.db.getUserNameAndPassword(userName)
        if userName == accountName and check_password_hash(accountPassword, password):
            session['userName'] = userName
            g.userName = userName
            return redirect(url_for('home'))
        elif userName == accountName:
            msg = 'Please enter your password again.'
            flash(msg)
            return redirect(url_for('signin'))
        else:
            msg = 'Account does not exist.'
            flash(msg)
            return redirect(url_for('signin'))
            
@app.route('/about', methods = ['GET'])
def about():
    if request.method == 'GET':
        return render_template('about.html', userName = g.userName)

if __name__ == '__main__':
    app.run(debug=True)
