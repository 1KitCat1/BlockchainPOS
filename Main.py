from Transaction import Transaction
from Wallet import Wallet
import copy

if __name__ == "__main__":
    transaction = Transaction(senderPK="sender",
                              receiverPK="receiver",
                              amount=1,
                              transactionType="TRANSFER")
    wallet = Wallet()
    anotherWallet = Wallet()

    transaction = wallet.createTransaction(receiverPK="receiverPublicKey",
                                           amount=1, 
                                           transactionType="TRANSFER")

    print(transaction.toJSON())
    print(Wallet.isSignatureValid(data=transaction.getPayload(), 
                                  signature=transaction.signature, 
                                  publicKeyString=wallet.getPublicKey()))
    print(transaction.isEqual(copy.deepcopy(transaction)))
    