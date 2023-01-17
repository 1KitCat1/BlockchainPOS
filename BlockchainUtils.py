from Crypto.Hash import SHA256
import json

class BlockchainUtils:
    @staticmethod
    def hash(data):
        dataString = json.dumps(data)
        dataBytes = dataString.encode('utf-8')
        return SHA256.new(dataBytes)