from Transaction import Transaction
from Wallet import Wallet


if __name__ == "__main__":
    transaction = Transaction(senderPK="sender",
                              receiverPK="receiver",
                              amount=1,
                              transactionType="TRANSFER")
    wallet = Wallet()
    signature = wallet.sign(transaction.toJSON())
    transaction.setSignature(signature=signature)

    print(transaction.toJSON())