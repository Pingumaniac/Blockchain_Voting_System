from flask import Flask, Blueprint, g, render_template, request, redirect, url_for, session, jsonify, flash, escape
from flask_bootstrap import Bootstrap
from simayiAPI.sqlAPI import DB
from werkzeug.security import check_password_hash

my_pages = Blueprint("my_pages", __name__, static_folder="static", template_folder="templates")

@my_pages.route('/mypage', methods = ['GET'])
def mypage():
    if request.method == 'GET':
        if g.userName == None:
            msg = "Please login to access My Page."
            flash(msg)
            return redirect(url_for('signin')) 
        else:
            userID, userName, userPassword, userFullName, userEmail, userPublicKey, userPrivateKey  = g.db.getUserData(g.userName)       
            return render_template('/my_pages/mypage.html', userID = userID, userName = g.userName, 
                                   userFullName = userFullName, userEmail = userEmail, 
                                   userPublicKey = userPublicKey, userPrivateKey = userPrivateKey)

@my_pages.route('/delete_account', methods = ['GET'])
def delete_account():
    if request.method == 'GET':
        if g.userName == None:
            msg = "Please login to access Delete Account Page."
            flash(msg)
            return redirect(url_for('signin')) 
        else:
            return render_template('/my_pages/delete_account.html', userName = g.userName)

@my_pages.route('/submit_delete_account_request', methods = ['POST'])
def submit_delete_account_request():
    if request.method == 'POST':
        data = request.get_json()
        print(data)
        currentID = data['currentID']
        currentPassword = data['currentPassword']
        
        if currentID != g.userName:
            return jsonify({'success': False})
        else:
            accountName, accountPassword = g.db.getUserNameAndPassword(currentID)
            if currentID == accountName and check_password_hash(accountPassword, currentPassword):
                g.db.deleteUser(currentID)
                return jsonify({'success': True})