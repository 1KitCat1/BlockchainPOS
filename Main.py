from Transaction import Transaction
from Wallet import Wallet
from Block import Block
from TransactionPool import TransactionPool
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
    block = wallet.createBlock(transactions=pool.transactions,
                               previousHash="00000",
                               blockCount=1)
    pprint.pprint(block.toJSON())
    print("Is signature valid: ", wallet.isSignatureValid(data=block.payload(), 
                                                          signature=block.signature,
                                                          publicKeyString=wallet.getPublicKey()))
    