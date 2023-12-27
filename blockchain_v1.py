import hashlib
import time

class Block:
    def __init__(self, transactions, prev_hash):
        self.transactions = transactions
        self.prev_hash = prev_hash
        self.timestamp = time.time()
        self.hash = self.calc_hash()

    def calc_hash(self):
        sha = hashlib.sha256()
        sha.update((str(self.transactions) + str(self.prev_hash) + str(self.timestamp)).encode('utf-8'))
        return sha.hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block([], "0")

    def add_block(self, transactions):
        prev_block = self.chain[-1]
        new_block = Block(transactions, prev_block.hash)
        self.chain.append(new_block)

blockchain = Blockchain()
blockchain.add_block(transactions=[{'sender' : 'Adnan', 'recipient' : 'Julie', 'Amount' : 5}])
blockchain.add_block(transactions=[{'sender' : 'Adnan', 'recipient' : 'Navin', 'Amount' : 4}])
blockchain.add_block(transactions=[{'sender' : 'Adnan', 'recipient' : 'Mohamed', 'Amount' : 7}])

print("Blockchain:")
for block in blockchain.chain:
    print("Data", block.transactions)
    print("Previous Hash:", block.prev_hash)
    print("Hash:", block.hash)
    print("Timestamp: ", block.timestamp)
    print()
