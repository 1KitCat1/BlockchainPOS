from p2pnetwork.node import Node as p2pNode
from PeerDiscovery import PeerDiscovery
from SocketConnector import SocketConnector
import SetupParameters

class SocketCommunication(p2pNode):
    def __init__(self, ip, port) -> None:
        super(SocketCommunication, self).__init__(host=ip, port=port)
        self.peers = []
        self.peerDiscoveryHandler = PeerDiscovery(self)
        self.socketConnector = SocketConnector(ip, port)
    
    def connectToFirstNode(self):
        if self.socketConnector.port != SetupParameters.DEFAULT_NODE_PORT \
            and self.socketConnector.ip != SetupParameters.DEFAULT_NODE_IP:

            self.connect_with_node(SetupParameters.DEFAULT_NODE_IP, SetupParameters.DEFAULT_NODE_PORT)
        
    def startSocketCommunication(self):
        self.start()
        self.peerDiscoveryHandler.start()
        self.connectToFirstNode()
    
    def inbound_node_connected(self, node):
        self.peerDiscoveryHandler.handshake(node)

    def outbound_node_connected(self, node):
        self.peerDiscoveryHandler.handshake(node)

    def node_message(self, connected_node, message):
        print(message)

    def send(self, receiver, message):
        self.send_to_node(receiver, message)
    
    def broadcats(self, message):
        self.send_to_nodes(message)