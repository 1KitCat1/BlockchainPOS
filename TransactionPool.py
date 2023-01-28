

class TransactionPool():

    def __init__(self) -> None:
        self.transactions = {}
    
    def addTransaction(self, transaction):
        transactionHash = transaction.getHashString()
        self.transactions[transactionHash] = transaction
    
    def transactionExists(self, transaction):
        transactionHash = transaction.getHashString()
        return transactionHash in self.transactions

    def getTransactionList(self):
        transactionList = []
        for transaction in self.transactions.values():
            transactionList.append(transaction)
        return transactionList

    def removeFromPool(self, transactions):
        for transaction in transactions:
            self.transactions.pop(transaction.getHashString(), '')
        