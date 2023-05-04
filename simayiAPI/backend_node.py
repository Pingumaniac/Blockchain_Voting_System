import sys
from flask import Flask, jsonify, request
from signature_verification import verify_signature
from backend_utils import Backend

app = Flask(__name__)
internal_state = None

@app.route('/add_user', methods=['GET'])
def add_user():
	username = request.args.get("username")
	public_key = request.args.get("public_key")
	response = (internal_state.get_user(username) is None)
	if (response):
		internal_state.set_user(username, public_key)
	result = {"username": username, "public_key": public_key, "response": response}
	return jsonify(result);

@app.route('/get_users', methods=['GET'])
def get_users():
	return jsonify(internal_state.get_user_list());

@app.route('/get_elections', methods=['GET'])
def get_elections():
	return jsonify(internal_state.get_election_list())

def unescape_json_string(str):
	# bytes(request.args.get("state"), "utf-8").decode("unicode_escape")
	return str

@app.route('/share_block', methods=['GET'])
def share_block():
	state = unescape_json_string(request.args.get("state"))
	transition = unescape_json_string(request.args.get("transition"))
	prev_hash = unescape_json_string(request.args.get("prev_hash"))
	new_hash = unescape_json_string(request.args.get("new_hash"))
	nonce = int(request.args.get("nonce"))
	forked_block = {'state': state, 'transition': transition, 'prev_hash': prev_hash, 'new_hash': new_hash, 'nonce': nonce}
	internal_state.commit_forked_block_no_processing(forked_block)
	return jsonify({});

@app.route('/add_election', methods=['GET'])
def add_election():
	name = request.args.get("name")
	prompt = request.args.get("prompt")
	username = request.args.get("username")
	signature = request.args.get("signature")
	response = verify_signature(internal_state.get_public_key(username), name + prompt + username, signature) and (internal_state.get_election(name) is None)
	if (response):
		internal_state.set_election(name, prompt, username, signature)
	result = {"name": request.args.get("name"), "prompt": prompt, "username": username, "signature": signature, "response": response}
	return jsonify(result);

@app.route('/add_vote', methods=['GET'])
def add_vote():
	name = request.args.get("name")
	username = request.args.get("username")
	vote = request.args.get("vote")
	signature = request.args.get("signature")
	response = verify_signature(internal_state.get_public_key(username), name + username + vote, signature) and internal_state.valid_vote(name, username, vote)
	if (response):
		internal_state.increment_election(name, username, vote, signature)
	result = {"name": name, "username": username, "vote": vote, "signature": signature, "response": response}
	return jsonify(result);

if __name__ == '__main__':
	app.config['data_folder'] = sys.argv[1]
	internal_state = Backend(app.config['data_folder'])
	port = sys.argv[2]
	app.run(debug=False, host="0.0.0.0", port=port)
