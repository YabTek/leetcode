class Bank:

    def __init__(self, balance: List[int]):
        self.balance = balance
        self.size = len(self.balance)
        
    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if (account1-1 < 0) or (account1 > self.size) : 
            return False 
        elif (account2-1 < 0) or (account2 > self.size) : 
            return False
        elif money > self.balance[account1-1] :
            return False 
        else : 
            self.balance[account1-1] -= money 
            self.balance[account2-1] += money 
            return True 
            
    def deposit(self, account: int, money: int) -> bool:
        
        if account-1 >=0 and account-1 < self.size:
            self.balance[account-1] += money
            return True
        else:
            return False
        
    def withdraw(self, account: int, money: int) -> bool:

        if account-1 >=0 and account-1 < self.size and self.balance[account-1] >= money:
                self.balance[account-1] -= money
                return True
        else:
                return False


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)