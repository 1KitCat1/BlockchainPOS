from Transaction import Transaction
from Wallet import Wallet
from Block import Block
from TransactionPool import TransactionPool
from Blockchain import Blockchain
from BlockchainUtils import BlockchainUtils
from AccountModel import AccountModel
import copy
import pprint


if __name__ == "__main__":
    wallet = Wallet()
    accountModel = AccountModel()

    print(accountModel.getBalance(walletPK=wallet.getPublicKey()))
    print(accountModel.balances)
