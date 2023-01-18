

class TransactionPool():

    def __init__(self) -> None:
        self.transactions = []
    
    def addTransaction(self, transaction):
        self.transactions.append(transaction)
    
    def transactionExists(self, transaction):
        # TODO: optimize with set
        transactionHash = transaction.getHash()
        for poolTansaction in self.transactions:
            if poolTansaction.getHash() == transactionHash:
                return True
        return False
