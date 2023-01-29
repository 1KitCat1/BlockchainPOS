from TransactionPool import TransactionPool
from Wallet import Wallet
from Blockchain import Blockchain
from SocketCommunication import SocketCommunication

class Node:
    
    def __init__(self, ip, port) -> None:
        self.transactionPool = TransactionPool()
        self.wallet = Wallet()
        self.blockchain = Blockchain()
        self.ip = ip
        self.port = port
        self.p2pCommunication = SocketCommunication(ip, port)
    
    def p2pStart(self):
        self.p2pCommunication.startSocketCommunication()