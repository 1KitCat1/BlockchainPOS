import time


class Transaction:
    def __init__(self, senderPK, receiverPK, amount, transactionType) -> None:
        self.senderPK = senderPK
        self.receiverPK = receiverPK
        self.amount = amount
        self.transactionType = transactionType
        self.timestamp = time.time()
        self.signature = ""
    
    def toJSON(self):
        return self.__dict__