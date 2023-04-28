from flask import Blueprint, jsonify

blockchain_bp = Blueprint('blockchain', __name__)

consensus_node_urls = [
    'http://localhost:6000',
    'http://localhost:6001',
    'http://localhost:6002'
]

import hashlib
import json
import time

class Block:
    def __init__(self, index, transactions, timestamp, previous_hash):
        self.index = index
        self.transactions = transactions
        self.timestamp = timestamp
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        # calculate the hash of the block
        block_string = json.dumps(self.__dict__, sort_keys=True)
        return hashlib.sha256(block_string.encode()).hexdigest()

    def mine(self, difficulty):
        # find a hash that satisfies the difficulty level
        target = '0' * difficulty
        while self.hash[:difficulty] != target:
            self.nonce += 1
            self.hash = self.calculate_hash()

class Blockchain:
    def __init__(self):
        self.chain = [Block(0, [], time.time(), '')]
        self.pending_transactions = []
        self.difficulty = 4

    def add_transaction(self, transaction):
        self.pending_transactions.append(transaction)

    def mine_block(self):
        block = Block(len(self.chain), self.pending_transactions, time.time(), self.chain[-1].hash)
        block.mine(self.difficulty)
        self.chain.append(block)
        self.pending_transactions = []

    def is_valid(self):
        # validate the blockchain
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i-1]
            if current_block.hash != current_block.calculate_hash():
                return False
            if current_block.previous_hash != previous_block.hash:
                return False
        return True

    def to_dict(self):
        # return the blockchain data as a dictionary
        return {
            'chain': [block.__dict__ for block in self.chain],
            'length': len(self.chain)
        }

class Transaction:
    def __init__(self, voter_id, candidate_id, signature, election_name):
        self.voter_id = voter_id
        self.candidate_id = candidate_id
        self.signature = signature
        self.election_name = election_name

    def to_dict(self):
        # return the transaction data as a dictionary
        return {
            'voter_id': self.voter_id,
            'candidate_id': self.candidate_id,
            'signature': self.signature,
            'election_name': self.election_name
        }

    @classmethod
    def from_dict(cls, data):
        # create a new transaction from dictionary data
        return cls(
            data['voter_id'],
            data['candidate_id'],
            data['signature'],
            data['election_name']
        )

blockchain = Blockchain()

@blockchain_bp.route('/blockchain', methods=['GET'])
def get_blockchain():
    return jsonify(blockchain.to_dict()), 200

@blockchain_bp.route('/transaction', methods=['POST'])
def add_transaction():
    transaction_data = request.get_json()
    transaction = Transaction.from_dict(transaction_data)
    
    # add the transaction to the transaction pool
    blockchain.add_transaction(transaction)
    
    # return a success message
    return jsonify({'message': 'Transaction added to pool'}), 200

@blockchain_bp.route('/mine', methods=['POST'])
def mine():
    # mine a new block and add it to the blockchain
    blockchain.mine_block()
    
    # broadcast the new block to the consensus nodes
    for url in consensus_node_urls:
        requests.post(url+'/block', json=blockchain.chain[-1].to_dict())
    
    # return a success message
    return jsonify({'message': 'Block mined and added to chain'}), 200

@blockchain_bp.route('/block', methods=['POST'])
def receive_block():
    block_data = request.get_json()
    block = Block.from_dict(block_data)
    
    # add the block to the blockchain
    blockchain.chain.append(block)
    
    # return a success message
    return jsonify({'message': 'Block received and added to chain'}), 200

def reach_consensus():
    # get the blockchain data from all consensus nodes
    blockchains = []
    for url in consensus_node_urls:
        response = requests.get(url+'/blockchain')
        blockchains.append(response.json())
    
    # choose the longest blockchain
    longest_chain = blockchain.chain
    for chain in blockchains:
        if len(chain) > len(longest_chain):
            longest_chain = chain
    
    # replace the local blockchain with the longest one
    blockchain.chain = longest_chain

@blockchain_bp.route('/consensus', methods=['GET'])
def consensus():
    # attempt to reach consensus with the other nodes
    reach_consensus()
    
    # return a success message
    return jsonify({'message': 'Blockchain updated to longest chain'}), 200
