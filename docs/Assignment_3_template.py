# Bank Management System
# Fill in all sections marked with TODO


import os
# TODO: Create two custom exception classes.
# Both must inherit from Exception.


class InsufficientFundsError(Exception):
    pass  # No changes needed here — just inheriting is enough!

class InvalidAmountError(Exception):
    pass  # No changes needed here — just inheriting is enough!


# BankAccount Class

class BankAccount:

    # TASK 1
    def __init__(self, account_number, owner_name, balance=0.0):
        # TODO: Assign the three parameters to instance attributes
        pass

    def __str__(self):
        # TODO: Return a string like:
        # "Account [ACC001] | Owner: Alice | Balance: $500.0"
        pass

    # TASK 3
    def deposit(self, amount):
        # TODO: Raise InvalidAmountError if amount <= 0
        # TODO: Add amount to self.balance
        # TODO: Call self.log_transaction("DEPOSIT", amount)
        # TODO: Return the new balance
        pass

    def withdraw(self, amount):
        # TODO: Raise InvalidAmountError if amount <= 0
        # TODO: Raise InsufficientFundsError if amount > self.balance
        # TODO: Subtract amount from self.balance
        # TODO: Call self.log_transaction("WITHDRAW", amount)
        # TODO: Return the new balance
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



# TASK 6: Bank Class

class Bank:

    def __init__(self, bank_name):
        # TODO: Assign bank_name attribute
        # TODO: Create an empty dictionary called accounts
        pass

    def add_account(self, account):
        # TODO: Add account to self.accounts using account_number as key
        # Hint: self.accounts[account.account_number] = account
        pass

    def get_account(self, account_number):
        # TODO: Check if account_number is in self.accounts
        # TODO: If not found, raise KeyError with a friendly message
        # TODO: If found, return the account
        pass

    def show_all_accounts(self):
        # TODO: If no accounts, print "No accounts found."
        # TODO: Otherwise, print each account using its __str__
        pass

    def save_all_accounts(self, filename):
        # TODO: Open filename in write mode inside a try block
        # TODO: Write each account as: account_number,owner_name,balance
        # TODO: Catch IOError and print an error message
        pass

    @classmethod
    def load_all_accounts(cls, filename, bank_name="LoadedBank"):
        # TODO: Create a new Bank object using cls(bank_name)
        # TODO: Open the file and read line by line
        # TODO: For each line, split by "," and create a BankAccount
        # TODO: Add each account to the bank's accounts dictionary
        # TODO: Catch FileNotFoundError — print message, return empty bank
        # TODO: Catch ValueError — print message, return empty bank
        # TODO: Return the bank object
        pass


# TASK 7: Main Menu

def main():
    bank = Bank("SecureBank")

    while True:
        print("SecureBank Menu")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Save Bank Data")
        print("6. Load Bank Data")
        print("7. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            acc_num = input("Account Number: ").strip()
            name = input("Owner Name: ").strip()
            try:
                starting = float(input("Starting Balance: ").strip())
                # TODO: Create a BankAccount and add it to the bank
            except ValueError:
                print("Invalid starting balance. Please enter a number.")

        elif choice == "2":
            acc_num = input("Account Number: ").strip()
            try:
                # TODO: Get the account using bank.get_account()
                # TODO: Get the deposit amount from user (convert to float)
                # TODO: Call deposit() and print new balance
                pass
            except KeyError as e:
                print(str(e))
            except InvalidAmountError as e:
                print("Invalid amount: " + str(e))
            except ValueError:
                print("Please enter a valid number.")

        elif choice == "3":
            acc_num = input("Account Number: ").strip()
            try:
                # TODO: Get the account using bank.get_account()
                # TODO: Get the withdrawal amount from user (convert to float)
                # TODO: Call withdraw() and print new balance
                pass
            except KeyError as e:
                print(str(e))
            except InsufficientFundsError as e:
                print("Transaction failed: " + str(e))
            except InvalidAmountError as e:
                print("Invalid amount: " + str(e))
            except ValueError:
                print("Please enter a valid number.")

        elif choice == "4":
            acc_num = input("Account Number: ").strip()
            try:
                # TODO: Get the account and print its balance
                pass
            except KeyError as e:
                print(str(e))

        elif choice == "5":
            filename = input("Save to filename: ").strip()
            # TODO: Call bank.save_all_accounts(filename)

        elif choice == "6":
            filename = input("Load from filename: ").strip()
            # TODO: Call Bank.load_all_accounts() and reassign bank

        elif choice == "7":
            print("Thank you for using SecureBank. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 7.")


if __name__ == "__main__":
    main()