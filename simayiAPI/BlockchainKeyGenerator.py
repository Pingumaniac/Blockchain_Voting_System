import hashlib
import secrets

class BlockchainKeyGenerator:
    def __init__(self):
        self.private_key = None
        self.public_key = None

    def generate_keys(self):
        self.private_key = secrets.token_hex(32) # generate 256-bit random string as private key
        self.public_key = hashlib.sha256(self.private_key.encode('utf-8')).hexdigest() # calculate SHA-256 hash of private key as public key

        return self.private_key, self.public_key
    
    def sign_transaction(self, transaction):
        # Calculate the SHA-256 hash of the transaction
        transaction_hash = hashlib.sha256(transaction.encode('utf-8')).hexdigest()
        
        # Use the private key to sign the transaction
        signature = hashlib.sha256((transaction_hash + self.private_key).encode('utf-8')).hexdigest()
        
        return signature
