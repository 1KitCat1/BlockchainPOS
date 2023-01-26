from Block import Block
from BlockchainUtils import BlockchainUtils


class Blockchain():
    
    def __init__(self) -> None:
        self.blocks = [Block.getGenesis()]
    
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