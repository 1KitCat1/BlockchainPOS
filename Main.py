from Transaction import Transaction
from Wallet import Wallet
from Block import Block
from TransactionPool import TransactionPool
import copy

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
    block = Block(transactions=pool.transactions,
                  previousHash="00000",
                  forgerPK="forger",
                  blockCount=1)
    print(block.toJSON())
    