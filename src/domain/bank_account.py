from .bank import Bank

class BankAccount(Bank):
    
    def __init__(self, account_number: str, owner_name: str, balance: float = 0.0):
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = balance
        
    def __str__(self):
        return f"Account: [{self.account_number}] | Owner: {self.owner_name}] | Balance: ${self.balance:.2f}"
        
    def make_deposit(self, amount: float=0.0):
                                            
        if amount > 0:
            self.balance += amount
            return f"Deposited ${amount:.2f}. New balance is ${self.balance:.2f}."
        else:
            return f"Invalid deposit amount. Please enter a positive dollar amount."
                                   
    def make_withdrawl(self, amount: float=0.0):
        
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                return f"Withdrew ${amount:.2f}. New balance is ${self.balance:.2f}."
        else:
            return f"Insufficient funds. Current balance is ${self.balance:.2f}."
                