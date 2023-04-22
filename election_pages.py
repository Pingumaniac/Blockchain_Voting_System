from flask import Flask, Blueprint, g, render_template, request, redirect, url_for, session, jsonify, flash, escape
from flask_bootstrap import Bootstrap
import pymysql
from simayiAPI.sqlAPI import DB

election_pages = Blueprint("election_pages", __name__, static_folder="static", template_folder="templates")

@election_pages.route('/elections/past', methods = ['GET'])
def past_elections():
    if request.method == 'GET':
        return render_template('/elections/past_elections.html', userName = g.userName)
    
@election_pages.route('/elections/current', methods = ['GET'])
def current_elections():
    if request.method == 'GET':
        return render_template('/elections/current_elections.html', userName = g.userName)

@election_pages.route('/my_elections/create', methods = ['GET'])
def create_elections():
    if request.method == 'GET':
        return render_template('/elections/create_elections.html', userName = g.userName)
    
@election_pages.route('/my_elections/view', methods = ['GET'])
def my_elections():
    if request.method == 'GET':
        return render_template('/elections/my_elections.html', userName = g.userName)