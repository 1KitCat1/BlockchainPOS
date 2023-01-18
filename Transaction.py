import time
import copy
import uuid

class Transaction:
    def __init__(self, senderPK, receiverPK, amount, transactionType) -> None:
        self.senderPK = senderPK
        self.receiverPK = receiverPK
        self.amount = amount
        self.transactionType = transactionType
        self.nonce = uuid.uuid4().hex
        self.timestamp = time.time()
        self.signature = ""

    def toJSON(self):
        return self.__dict__

    def setSignature(self, signature):
        self.signature = signature

    def payload(self):
        transactionJSON = copy.deepcopy(self.toJSON())
        transactionJSON["signature"] = ""
        return transactionJSON
