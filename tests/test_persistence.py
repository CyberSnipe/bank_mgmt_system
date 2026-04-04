from domain.bank_account import BankAccount
from persistence.bank_repository import BankRepository
from domain.bank import Bank
from routing.cli_menu import main

# Test 6: Save and Load Single Account
print("Test 6: Save and Load Single Account")
acc.save_account("test_acc.json")
loaded_acc = BankAccount.load_account("test_acc.json")
assert loaded_acc.account_number == "ACC001"
assert loaded_acc.owner_name == "Alice"
assert loaded_acc.balance == 650.0

print("Test sat!")

# Test 7: Load Missing File
print("Test 7: Load Missing File")
result = BankAccount.load_account("ghost_file.txt")
assert result is None # Should return None and print an error
print("Test sat!")

# Test 10: Save and Load Bank
print("Test 10: Save and Load Bank")
BankRepository.save_all(bank, "test_bank.json")
loaded_bank = BankRepository.load_all("test_bank.json")
assert len(loaded_acc.accounts) == 2
assert "ACC003" in loaded_acc.accounts
print("Test sat!")