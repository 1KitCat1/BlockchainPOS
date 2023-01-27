

class AccountModel:
    def __init__(self) -> None:
        self.balances = {}
    
    def safeInitAccount(self, walletPK):
        if walletPK not in self.balances:
            self.balances[walletPK] = 0
    
    def getBalance(self, walletPK):
        self.safeInitAccount(walletPK)
        return self.balances[walletPK]
    
    def addBalance(self, walletPK, balanceChange):
        self.safeInitAccount(walletPK)
        self.balances[walletPK] += balanceChange
