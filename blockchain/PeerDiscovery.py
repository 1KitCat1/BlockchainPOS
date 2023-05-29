import threading
import time


class PeerDiscovery():

    def __init__(self, node) -> None:
        self.socketCommunication = node
    
    # Searching for new nodes in the network
    def discovery(self):
        while True:
            print('Searching for new nodes...')
            time.sleep(5)

    def status(self):
        while True:
            print("Updating status...")
            time.sleep(5)
        
    def start(self):
        discoveryTread = threading.Thread(target=self.discovery)
        discoveryTread.start()
        statusThread = threading.Thread(target=self.status)
        statusThread.start()

    def handshake(self, connect_node):
        # TODO: replace "Handshake" placeholder with data about other nodes
        self.socketCommunication.send(connect_node, "Handshake")