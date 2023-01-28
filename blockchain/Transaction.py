import time
import copy
import uuid
from BlockchainUtils import BlockchainUtils

class Transaction:
    def __init__(self, senderPK, receiverPK, amount, transactionType) -> None:
        self.senderPK = senderPK
        self.receiverPK = receiverPK
        self.amount = amount
        self.type = transactionType
        self.nonce = uuid.uuid4().hex
        self.timestamp = time.time()
        self.signature = ""

    def toJSON(self):
        return self.__dict__

    def setSignature(self, signature):
        self.signature = signature

    def getPayload(self):
        transactionJSON = copy.deepcopy(self.toJSON())
        transactionJSON["signature"] = ""
        return transactionJSON
    
    def getHashString(self):
        return BlockchainUtils.hash(self.toJSON()).hexdigest()

    def isEqual(self, other):
        return self.getHashString == other.getHashString
