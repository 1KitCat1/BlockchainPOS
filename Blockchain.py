from Block import Block
from BlockchainUtils import BlockchainUtils
from AccountModel import AccountModel
from TransactionTypes import TransactionTypes

class Blockchain:
    
    def __init__(self) -> None:
        self.blocks = [Block.getGenesis()]
        self.accountModel = AccountModel()
    
    def addBlock(self, block):
        self.blocks.append(block)
    
    def toJSON(self) -> dict:
        jsonBlocks = []
        for block in self.blocks:
            jsonBlocks.append(block.toJSON())
        return {'blocks' : jsonBlocks}

    def isBlockCountValid(self, block) -> bool:
        return self.blocks[-1].blockCount == block.blockCount - 1

    def isPreviousHashValid(self, block) -> bool:
        previousHash = BlockchainUtils.hash(self.blocks[-1].payload()).hexdigest()
        return previousHash == block.previousHash
    
    def isTransactionCovered(self, transaction):
        if transaction.type == TransactionTypes.FORGE:
            return True
        senderBalance = self.accountModel.getBalance(transaction.senderPK) 
        return senderBalance >= transaction.amount

    def getCoveredTransactions(self, transactions):
        coveredTransactions = []
        for transaction in transactions:
            if self.isTransactionCovered(transaction):
                coveredTransactions.append(transaction)
        return coveredTransactions
