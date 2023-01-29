from p2pnetwork.node import Node as p2pNode


class SocketCommunication(p2pNode):
    def __init__(self, ip, port) -> None:
        super(SocketCommunication, self).__init__(host=ip, port=port)

    def startSocketCommunication(self):
        self.start()
        