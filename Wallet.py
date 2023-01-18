from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from BlockchainUtils import BlockchainUtils
from Transaction import Transaction

class Wallet:

    def __init__(self) -> None:
        self.keyPair = RSA.generate(2048)
    
    def sign(self, data):
        dataHash = BlockchainUtils.hash(data)
        signatureScheme = PKCS1_v1_5.new(self.keyPair)
        signature = signatureScheme.sign(dataHash)
        return signature.hex()

    @staticmethod
    def isSignatureValid(data, signature, publicKeyString):
        signature = bytes.fromhex(signature)
        dataHash = BlockchainUtils.hash(data)
        publicKeyRSA = RSA.importKey(publicKeyString)
        signatureScheme = PKCS1_v1_5.new(rsa_key=publicKeyRSA)
        return signatureScheme.verify(dataHash, signature=signature)
    
    def getPublicKey(self):
        return self.keyPair.publickey().exportKey().decode('utf-8')
    
    def createTransaction(self, receiverPK, amount, transactionType):
        transaction = Transaction(senderPK=self.getPublicKey(),
                                  receiverPK=receiverPK,
                                  amount=amount,
                                  transactionType=transactionType)
        signature = self.sign(transaction.getPayload())
        transaction.setSignature(signature)
        return transaction