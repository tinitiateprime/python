# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : Custom Exceptions
#  Author       : Team Tinitiate
# ==============================================================================



class InsufficientFundsError(Exception):
    pass

class Account:
    def __init__(self, balance):
        self.balance = balance
    
    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError
            ("Insufficient funds to withdraw " + str(amount))
        self.balance -= amount
        print("Withdrawal successful. Remaining balance:", self.balance)

try:
    acc = Account(1000)
    acc.withdraw(1500)
except InsufficientFundsError as e:
    print("Error:", e)
# OUTPUT: Error: 
