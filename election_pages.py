from flask import Flask, Blueprint, g, render_template, request, redirect, url_for, session, jsonify, flash, escape
from flask_bootstrap import Bootstrap
import pymysql
import json
from datetime import date

election_pages = Blueprint("election_pages", __name__, static_folder="static", template_folder="templates")

    
@election_pages.route('/elections/view', methods = ['GET'])
def view_elections():
    if request.method == 'GET':
        return render_template('/elections/view_elections.html')

@election_pages.route('/elections/create', methods = ['GET'])
def create_elections():
    if request.method == 'GET':
        return render_template('/elections/create_elections.html')
    
@election_pages.route('/elections/vote', methods = ['GET'])
def vote_elections():
    if request.method == 'GET':
        return render_template('/elections/vote.html')