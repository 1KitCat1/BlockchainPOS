from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from BlockchainUtils import BlockchainUtils


class Wallet:
    def __init__(self) -> None:
        self.keyPair = RSA.generate(2048)
    
    def sign(self, data):
        dataHash = BlockchainUtils.hash(data)
        signatureScheme = PKCS1_v1_5.new(self.keyPair)
        signature = signatureScheme.sign(dataHash)
        return signature.hex()
