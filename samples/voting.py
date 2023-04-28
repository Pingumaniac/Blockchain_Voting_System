from flask import Blueprint, jsonify
from functools import wraps
from random import randint

voting_bp = Blueprint('voting', __name__)

load_balancer_urls = [
    'http://localhost:5000',
    'http://localhost:5001',
    'http://localhost:5002'
]

token_list = {
    'token1': 'user1',
    'token2': 'user2'
}

def token_required(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')
        if token and token in token_list:
            return func(*args, **kwargs)
        else:
            return jsonify({'error': 'Unauthorized'}), 401
    return decorated

def validate_voter(voter_id):
    # validate the voter ID
    return True

def validate_candidate(candidate_id):
    # validate the candidate ID
    return True

def validate_signature(voter_id, signature):
    # validate the voter's signature
    return True

def has_voted(voter_id, blockchain):
    # check if the voter has already voted in this election
    return False

def validate_election(election_name, candidate_id, blockchain):
    # validate the election and candidate IDs
    return True

@voting_bp.route('/vote', methods=['POST'])
@token_required
def vote():
    data = request.get_json()
    voter_id = data['voter_id']
    candidate_id = data['candidate_id']
    signature = data['signature']
    election_name = data['election_name']
    
    # validate the inputs
    if not validate_voter(voter_id):
        return jsonify({'error': 'Invalid voter ID'}), 400
    if not validate_candidate(candidate_id):
        return jsonify({'error': 'Invalid candidate ID'}), 400
    if not validate_signature(voter_id, signature):
        return jsonify({'error': 'Invalid signature'}), 400
    if has_voted(voter_id, blockchain):
        return jsonify({'error': 'Already voted'}), 400
    if not validate_election(election_name, candidate_id, blockchain):
        return jsonify({'error': 'Invalid election'}), 400
    
    # create a new transaction
    transaction = Transaction(voter_id, candidate_id, signature, election_name)
    
    # choose a random load balancer to send the transaction to
    url = load_balancer_urls[randint(0, len(load_balancer_urls)-1)]
    
    # send the transaction to the load balancer
    response = requests.post(url+'/transaction', json=transaction.to_dict())
    
    # return the response from the load balancer
    return jsonify(response.json()), response.status_code
