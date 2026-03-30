from src.domain.bank import Bank

class BankAccount(Bank):
    """BankAccount class representing a single bank account with an account number, owner name, and balance."""
    
    def __init__(self, account_number: str, owner_name: str, balance: float = 0.0):
        """Constructor to initialize a bank account with an account number, owner name, and an optional balance (default is 0.0)."""
        
        super().__init__(bank_name="SecureBank", accounts={})
        """ 
        Initialize the BankAccount with the provided account number, owner name, and balance. 
        The bank name is set to "SecureBank" and the accounts dictionary is initialized as empty. 
        """
        
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = balance
        
    def __str__(self):
        """String representation of the bank account showing the account number, owner name, and balance formatted to two decimal places."""
        
        return f"Account: [{self.account_number}] | Owner: {self.owner_name}] | Balance: ${self.balance:.2f}"
    
    def __repr__(self):
        """Official representation of the bank account showing the account number, owner name, and balance in a more detailed format."""
        
        return f"BankAccount(account_number='{self.account_number}', owner_name='{self.owner_name}', balance={self.balance})"
        
    def make_deposit(self, amount: float=0.0):
        """Deposits a specified amount into the bank account. The amount must be a positive dollar amount. Returns a message indicating the result of the deposit."""
                                            
        if amount > 0:
            self.balance += amount
            return f"Deposited ${amount:.2f}. New balance is ${self.balance:.2f}."
        else:
            return f"Invalid deposit amount. Please enter a positive dollar amount."
                                   
    def make_withdrawl(self, amount: float=0.0):
        """
        Withdraws a specified amount from the bank account. The amount must be a 
        positive dollar amount and less than or equal to the current balance. 
        Returns a message indicating the result of the withdrawal.
        """
        
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                return f"Withdrew ${amount:.2f}. New balance is ${self.balance:.2f}."
        else:
            return f"Insufficient funds. Current balance is ${self.balance:.2f}."
            
            
account1 = BankAccount("ACC001", "Alice", 500.0)
print(account1)