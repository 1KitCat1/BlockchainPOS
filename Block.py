import time
import copy
from Transaction import Transaction


class Block:

    def __init__(self, transactions, previousHash, forgerPK, blockCount) -> None:
        self.transactions = transactions
        self.previousHash = previousHash
        self.forgerPK = forgerPK
        self.blockCount = blockCount
        self.timestamp = time.time()
        self.signature = ""
    
    def toJSON(self):
        data = copy.deepcopy(self.__dict__)
        data["transactions"] = []
        for transaction in self.transactions:
            data["transactions"].append(transaction.toJSON())
        return data


    