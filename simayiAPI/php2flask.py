from flask import Flask
import requests
import json

app = Flask(__name__)

@app.route('/add_election_php', methods = ['GET'])
def add_election_php():
    if request.method == 'GET':
        node_root = request.args.get("node_name")
        location = f"{node_root}/add_election?"
        args = {
            "name": request.args.get("name"),
            "prompt": request.args.get("prompt"),
            "username": request.args.get("username"),
            "signature": request.args.get("signature")
        }
        url_query = location + "&".join([f"{k}={v}" for k, v in args.items()])
        result = requests.get(url_query)
        resultJson = json.dumps(result.json())
        return resultJson

@app.route('/add_user_php', methods = ['GET'])
def add_user_php():
    if request.method == 'GET':
        node_root = request.args.get("node_name")
        location = f"{node_root}/add_user?"
        args = {
            "username": request.args.get("username"),
            "public_key": request.args.get("public_key")
        }
        url_query = location + "&".join([f"{k}={v}" for k, v in args.items()])
        result = requests.get(url_query)
        resultJson = json.dumps(result.json())
        return resultJson

@app.route('/add_vote_php', methods = ['GET'])
def add_vote_php():
    if request.method == 'GET':
        node_root = request.args.get("node_name")
        location = f"{node_root}/add_vote?"
        args = {
            "name": request.args.get("name"),
            "username": request.args.get("username"),
            "vote": request.args.get("vote"),
            "signature": request.args.get("signature")
        }
        url_query = location + "&".join([f"{k}={v}" for k, v in args.items()])
        result = requests.get(url_query)
        resultJson = json.dumps(result.json())
        return resultJson

@app.route('/get_current_elections_php', methods=['GET'])
def get_current_elections_php():
    if request.method == 'GET':
        node_root = request.args.get("node_name")
        url_query = f"{node_root}/get_current_elections"
        result = requests.get(url_query)
        resultJson = json.dumps(result.json())
        return resultJson

@app.route('/get_current_nodes_php', methods = ['GET'])
def get_current_nodes_php():
    if request.method == 'GET':
        all_data = ['http://ransom.isis.vanderbilt.edu:5000']
        return json.dumps(all_data)

@app.route('/get_current_users_php', methods = ['GET'])
def get_current_users_php():
    if request.method == 'GET':
        node_root = request.args.get("node_name")
        url_query = f"{node_root}/get_users"
        result = requests.get(url_query)
        resultJson = json.dumps(result.json())
        return resultJson

if __name__ == "__main__":
    app.run()
