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
    
    @staticmethod
    def getGenesis():
        genesisBlock = Block(transactions=[],
                             previousHash="00000000",
                             forgerPK="00000000",
                             blockCount=0)
        genesisBlock.timestamp = 0 
        return genesisBlock

    def toJSON(self):
        data = copy.deepcopy(self.__dict__)
        data["transactions"] = []
        for transaction in self.transactions:
            data["transactions"].append(transaction.toJSON())
        return data

    def payload(self):
        json = copy.deepcopy(self.toJSON())
        json['signature'] = ''
        return json

    def sign(self, signature):
        self.signature = signature

    