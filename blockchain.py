import hashlib
import time

class Block:
    def __init__(self, index, previous_hash, data):
        self.index = index
        self.timestamp = time.time()
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        content = f"{self.index}{self.timestamp}{self.data}{self.previous_hash}{self.nonce}"
        return hashlib.sha256(content.encode()).hexdigest()

    def mine_block(self, difficulty=2):
        target = "0" * difficulty
        while self.hash[:difficulty] != target:
            self.nonce += 1
            self.hash = self.calculate_hash()
        print(f"Block Mined: {self.hash}")

# Initialize Blockchain with Genesis Block
genesis_block = Block(0, "0", "Genesis Block")
blockchain = [genesis_block]

# Add a second block
new_block = Block(1, genesis_block.hash, "Transaction: Alice sent 5 BTC to Bob")
new_block.mine_block(difficulty=2)
blockchain.append(new_block)
