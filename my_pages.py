from flask import Flask, Blueprint, g, render_template, request, redirect, url_for, session, jsonify, flash, escape
from flask_bootstrap import Bootstrap
import pymysql
from simayiAPI.sqlAPI import DB

my_pages = Blueprint("my_pages", __name__, static_folder="static", template_folder="templates")

@my_pages.route('/mypage', methods = ['GET'])
def mypage():
    if request.method == 'GET':
        # Prototype testing purposes only
        return render_template('/my_pages/mypage.html', userID = "TheGloriousPinguEmpire", 
                               userName = g.userName, userFullName = "Pingu Moon", 
                               userEmail = "pinguIsNotAClay@pingu.com", userPublicKey = "penguin", 
                               userPrivateKey = "IAMNOTACLAY")
        """
        if g.userName == None:
            msg = "Please login to access My Page."
            flash(msg)
            return redirect(url_for('signin')) 
        else:
            userID, userName, userPassword, userFullName, userEmail, userPublicKey, userPrivateKey  = g.db.getUserData(g.userName)       
            return render_template('/my_pages/mypage.html', userID = userID, userName = g.userName, 
                                   userFullName = userFullName, userEmail = userEmail, 
                                   userPublicKey = userPublicKey, userPrivateKey = userPrivateKey)
        """

@my_pages.route('/mypage/delete_account', methods = ['GET'])
def delete_account():
    if request.method == 'GET':
        # Prototype testing purposes only
        return render_template('/my_pages/delete_account.html', userName = g.userName)
        """
        if g.userName == None:
            msg = "Please login to access Delete Account Page."
            flash(msg)
            return redirect(url_for('signin')) 
        else:
            return render_template('/my_pages/delete_account.html', userName = g.userName)
        """