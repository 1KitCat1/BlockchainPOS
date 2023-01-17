from Crypto.PublicKey import RSA

class Wallet:
    def __init__(self) -> None:
        self.keyPair = RSA.generate(2048)
        