from flask import Flask, request, jsonify
import requests
from random import randint

from voting import voting_bp
from blockchain import blockchain_bp

app = Flask(__name__)

app.register_blueprint(voting_bp)
app.register_blueprint(blockchain_bp)


if __name__ == '__main__':
    app.run()
