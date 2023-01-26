from Transaction import Transaction
from Wallet import Wallet
from Block import Block
from TransactionPool import TransactionPool
from Blockchain import Blockchain
from BlockchainUtils import BlockchainUtils
import copy
import pprint


if __name__ == "__main__":
    transaction = Transaction(senderPK="sender",
                              receiverPK="receiver",
                              amount=1,
                              transactionType="TRANSFER")
    wallet = Wallet()
    anotherWallet = Wallet()

    transaction = wallet.createTransaction(receiverPK="receiverPublicKey",
                                           amount=1, 
                                           transactionType="TRANSFER")

    pool = TransactionPool()
    pool.addTransaction(transaction)
    # print(len(pool.transactions))
    blockchain = Blockchain()
    previousHash = BlockchainUtils.hash(blockchain.blocks[-1].payload()).hexdigest()

    block = wallet.createBlock(transactions=pool.transactions,
                               previousHash=previousHash,
                               blockCount=len(blockchain.blocks))

    # pprint.pprint(block.toJSON())
    # print("Is signature valid: ", wallet.isSignatureValid(data=block.payload(), 
    #                                                       signature=block.signature,
    #                                                       publicKeyString=wallet.getPublicKey()))
    
    if blockchain.isBlockCountValid(block) and blockchain.isPreviousHashValid(block):
        blockchain.addBlock(block=block)

    pprint.pprint(blockchain.toJSON())