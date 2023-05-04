from flask import Flask, Blueprint, g, render_template, request, redirect, url_for, session, jsonify, flash, escape
from flask_bootstrap import Bootstrap

user_pages = Blueprint("user_pages", __name__, static_folder="static", template_folder="templates")

@user_pages.route('/users/view', methods = ['GET'])
def view_users():
    if request.method == 'GET':
        return render_template('/users/view.html')
    
@user_pages.route('/users/create', methods = ['GET'])
def create_user():
    if request.method == 'GET':
        return render_template('/users/create.html')
