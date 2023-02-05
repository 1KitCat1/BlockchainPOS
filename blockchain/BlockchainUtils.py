from Crypto.Hash import SHA256
import json
import jsonpickle


class BlockchainUtils:
    @staticmethod
    def hash(data):
        dataString = json.dumps(data)
        dataBytes = dataString.encode('utf-8')
        return SHA256.new(dataBytes)

    @staticmethod
    def encode(value):
        return jsonpickle.encode(value=value)
    
    @staticmethod
    def decode(encodedValue):
        return jsonpickle.decode(encodedValue)
