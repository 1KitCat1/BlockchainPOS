from p2pnetwork.node import Node as p2pNode


class SocketCommunication(p2pNode):
    def __init__(self, ip, port) -> None:
        super(SocketCommunication, self).__init__(host=ip, port=port)

    def startSocketCommunication(self):
        self.start()
    
    def inbound_node_connected(self, node):
        print("Other node connected to this node")
        self.send_to_node(n=node, data="Message from connected node")
        # return super().inbound_node_connected(node)

    def outbound_node_connected(self, node):
        print("This node connected to other node")
        self.send_to_node(n=node, data="Message from main node")
        # return super().outbound_node_connected(node)    

    def node_message(self, connected_node, message):
        print(message)
        # return super().node_message(node, data)