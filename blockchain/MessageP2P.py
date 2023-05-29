

class MessageP2P:
    def __init__(self, socketConnector, messageType, data) -> None:
        self.socketConnector = socketConnector
        self.messageType = messageType
        self.data = data