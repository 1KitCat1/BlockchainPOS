from Transaction import Transaction

if __name__ == "__main__":
    transaction = Transaction(senderPK="sender",
                              receiverPK="receiver",
                              amount=1,
                              transactionType="TRANSFER")

    print(transaction.toJSON())