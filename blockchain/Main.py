from Transaction import Transaction
from Wallet import Wallet
from Block import Block
from TransactionPool import TransactionPool
from TransactionTypes import TransactionTypes
from Blockchain import Blockchain
from BlockchainUtils import BlockchainUtils
from AccountModel import AccountModel
from Node import Node
import copy
import pprint
import sys

if __name__ == "__main__":
    node = Node(ip=sys.argv[1], port=int(sys.argv[2]))
    node.p2pStart()

    if int(sys.argv[2]) == 10002:
      node.p2pCommunication.connect_with_node(host="localhost", port=10001)
    # alice = Wallet()
    # bob = Wallet()
    # blockchain = Blockchain()

    # transaction = alice.createTransaction(alice.getPublicKey(), 10, TransactionTypes.FORGE)
    # transactionPool = TransactionPool()

    # transactionPool.addTransaction(transaction=transaction)
    # transactionPool.addTransaction(transaction=transaction)
    
    # coveredTransactions = blockchain.getCoveredTransactions(transactionPool.getTransactionList())
    # block = Block(transactions=coveredTransactions,
    #               previousHash=BlockchainUtils.hash(blockchain.blocks[-1].payload()).hexdigest(),
    #               forgerPK=alice.getPublicKey(),
    #               blockCount=blockchain.blocks[-1].blockCount + 1
    #             )
    
    # blockchain.addBlock(block=block)
    # transactionPool.removeFromPool(transactions=block.transactions)
    # # pprint.pprint(blockchain.accountModel.balances)

    # transactionPool.addTransaction(
    #     transaction=alice.createTransaction(bob.getPublicKey(), 4, TransactionTypes.TRANSFER))
    

    # coveredTransactions = blockchain.getCoveredTransactions(transactionPool.getTransactionList())
    # block = Block(transactions=coveredTransactions,
    #               previousHash=BlockchainUtils.hash(blockchain.blocks[-1].payload()).hexdigest(),
    #               forgerPK=alice.getPublicKey(),
    #               blockCount=blockchain.blocks[-1].blockCount + 1
    #             )
    # # pprint.pprint(block.toJSON())
    # blockchain.addBlock(block=block)
    # pprint.pprint(blockchain.toJSON())
    # pprint.pprint(blockchain.accountModel.balances)
    
    # # pprint.pprint(block.toJSON())
    
    