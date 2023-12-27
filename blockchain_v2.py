import hashlib
import time
import graphviz

# Input of transaction of information

send = input("Who is the sender? ")
rec = input("Who is the recipient? ")
value = input("What is the amount? ")

# Creating class for the creation of individual blocks

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

# Creating class for the creation of the block (stringing along of blocks)
class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block([], "0")

    def add_block(self, transactions):
        prev_block = self.chain[-1]
        new_block = Block(transactions, prev_block.hash)
        self.chain.append(new_block)

# Function for visualising the blockchain as a png file

    def visualize(self):
        dot = graphviz.Digraph(comment='Blockchain')
        for i, block in enumerate(self.chain):
            if i == 0:
                dot.node(str(i),
                     f"Block {i}\nHash: {block.hash}\nPrev Hash: {block.prev_hash}\nTimestamp: {block.timestamp:.2f}")
            else:
                dot.node(str(i),
                         f"Block {i}\nSender: {send}\nRecipient: {rec}\nAmount: {value}\nHash: {block.hash}\nPrev Hash: {block.prev_hash}\nTimestamp: {block.timestamp:.2f}")
            if i > 0:
                dot.edge(str(i - 1), str(i))
        dot.render('blockchain', format='png', cleanup=True)
        print("Blockchain visualization created: 'blockchain.png'")

# blockchain transactions

blockchain = Blockchain()
blockchain.add_block(transactions=[{'sender' : send, 'recipient' : rec, 'Amount' : value}])
blockchain.visualize()
