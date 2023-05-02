from flask import Flask, Blueprint, g, render_template, request, redirect, url_for, session, jsonify, flash, escape
from flask_bootstrap import Bootstrap
import pymysql
from simayiAPI.sqlAPI import DB
import json
from datetime import date

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
    
@election_pages.route('/my_elections', methods = ['GET'])
def my_elections():
    if request.method == 'GET':
        return render_template('/elections/my_elections.html', userName = g.userName)

def custom_serializer(obj):
    if isinstance(obj, date):
        return obj.isoformat()
    raise TypeError(f"Type {type(obj)} is not JSON serializable")

@election_pages.route('/get_my_elections', methods = ['GET'])
def get_my_elections():
    if request.method == 'GET':
        userID = g.db.getUserID(g.userName)
        myElectionTable = g.db.getMyElection(userID)
        jsonElectionTable = json.dumps(myElectionTable, default=custom_serializer)
        return jsonElectionTable


@election_pages.route('/submit_create_election_request', methods = ['POST'])
def submit_create_election_request():
    if request.method == 'POST':
        data = request.get_json()
        electionTitle = data['title']
        electionPrompt = data['prompt']
        # electionUserName = data['username']
        electionPK = data['pk']
        electionEndDate = data['endDate']
        try:
            userName = str(escape(session['userName']))
            userID = g.db.getUserID(userName)
            g.db.addElection(electionTitle, electionPrompt, electionPK, electionEndDate,  userID)
            return jsonify({"success": True, "message": "Election created successfully."})
        except Exception as e:
            return jsonify({"success": False, "message": "There was an error creating the election."})
        

@election_pages.route('/elections/view_details', methods = ['GET'])
def view_election_details():
    if request.method == 'GET':
        return render_template('/elections/view_election_details.html', userName = g.userName)

