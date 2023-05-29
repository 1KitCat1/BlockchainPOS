
# Class for saving socket connection parameters
class SocketConnector():

    def __init__(self, ip, port) -> None:
        self.ip = ip
        self.port = port

    def equals(self, other):
        return self.ip == other.ip and self.port == other.port
