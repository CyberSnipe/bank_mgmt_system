# BankAccount Class
from domain.exceptions.invalid_amount_error import InvalidAmountError
from domain.exceptions.insufficient_funds_error import InsufficientFundsError

# TASK 1
class BankAccount:
    """Domain Class representing a bank account."""

    def __init__(self, account_number: str, owner_name: str, balance: float = 0.0):             # Assign the three parameters to instance attributes
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = balance

    def __str__(self):                                                                                              # Return a string like:        
        return f"Account: [{self.account_number}] | Owner: {self.owner_name} | Balance: ${self.balance:.2f}"        # "Account [ACC001] | Owner: Alice | Balance: $500.0"

    def __repr__(self):                                                                                             # Representation 
        return (
            f"BankAccount(account_number='{self.account_number}', "
            f"owner_name='{self.owner_name}', balance={self.balance})"
        )

    def make_deposit(self, amount: float):
        if amount <= 0:
            raise InvalidAmountError("Deposit amount must be positive.")        # Raise InvalidAmountError if amount <= 0
        self.balance += amount                                                  # Add amount to self.balance
        # self.log_transaction("DEPOSIT", amount)                                 # TODO Call self.log_transaction("DEPOSIT", amount)
        return self.balance                                                      # Return the new balance

    def make_withdrawl(self, amount: float):
        # TODO: Return the new balance
        if amount <= 0:
            raise InvalidAmountError("Withdrawal amount must be positive.")       # Raise InvalidAmountError if amount <= 0  
        if amount > self.balance:
            raise InsufficientFundsError("Insufficient funds for withdrawal.")     # Raise InsufficientFundsError if amount > self.balance 
        self.balance -= amount                                                     # Subtract amount from self.balance
        # self.log_transaction("WITHDRAW", amount)                                 # TODO: Call self.log_transaction("WITHDRAW", amount)
        return self.balance

    def log_transaction(self, transaction_type, amount):
        # TODO: Open "transactions.txt" in append mode inside a try block
        # TODO: Write a line like: [ACC001] DEPOSIT $200.0 | New Balance: $700.0
        # TODO: Catch OSError and print a message
        # TODO: Add a finally block that prints "Log attempt complete."    
        pass