# bank_service.py for business logic related to bank operations

from src.domain.bank import Bank
from src.data.bank_repo.json import BankRepository

class BankService:

    def __init__(self, bank_repository: BankRepository):
        self.bank_repository = bank_repository
        
    def create_bank(self, name: str, address: str) -> Bank:
        new_bank = Bank(name=name, address=address)
        return self.bank_repository.add_bank(new_bank)
    
    def get_bank(self, bank_id: int) -> Bank:
        return self.bank_repository.get_bank_by_id(bank_id)
    
    def update_bank(self, bank_id: int, name: str = None, address: str = None) -> Bank:
        pass
    
    def delete_bank(self, bank_id: int) -> bool:
        pass
    
    # TASK 4
    def log_transaction(self, transaction_type, amount):
        # TODO: Open "transactions.txt" in append mode inside a try block
        # TODO: Write a line like: [ACC001] DEPOSIT $200.0 | New Balance: $700.0
        # TODO: Catch OSError and print a message
        # TODO: Add a finally block that prints "Log attempt complete."
        pass

    # TASK 5
    def save_to_file(self, filename):
        # TODO: Open filename in write mode inside a try block
        # TODO: Write one line: account_number,owner_name,balance
        # TODO: Catch IOError and print a message
        pass

    @classmethod
    def load_from_file(cls, filename):
        # TODO: Open filename in read mode inside a try block
        # TODO: Read and split the line by ","
        # TODO: Validate that there are exactly 3 parts (raise ValueError if not)
        # TODO: Convert balance to float
        # TODO: Return a new BankAccount object using cls(...)
        # TODO: Catch FileNotFoundError — print message, return None
        # TODO: Catch ValueError — print message, return None
        pass
    
    
    