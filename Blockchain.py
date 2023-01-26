

class Blockchain():
    
    def __init__(self) -> None:
        self.blocks = []
    
    def addBlock(self, block):
        self.blocks.append(block)
    
    def toJSON(self) -> dict:
        jsonBlocks = []
        for block in self.blocks:
            jsonBlocks.append(block.toJSON())
        return {'blocks' : jsonBlocks}