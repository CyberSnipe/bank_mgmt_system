import json
from pathlib import Path
from domain.bank import Bank
from domain.bank_account import BankAccount

class BankRepository:
    """Repository for saving and loading all Bank accounts to/from JSON."""

    @staticmethod
    def load_all(filename: str, bank_name: str = "LoadedBank") -> Bank:
        """Load all accounts from a JSON file and return a Bank object."""
        file_path = Path(filename)

        # If file doesn't exist, return an empty bank
        if not file_path.exists():
            return Bank(bank_name)

        try:
            with open(filename, "r") as f:
                data = json.load(f)

            bank = Bank(bank_name)

            for entry in data:
                if not all(k in entry for k in ("account_number", "owner_name", "balance")):
                    continue  # skip malformed entries

                account = BankAccount(
                    account_number=entry["account_number"],
                    owner_name=entry["owner_name"],
                    balance=float(entry["balance"])
                )

                bank.add_account(account)

            return bank

        except (OSError, ValueError, json.JSONDecodeError):
            return Bank(bank_name)
        
    @staticmethod
    def save_all(bank: Bank, filename: str) -> None:
        """Save all accounts in the bank to a JSON file."""
        data = []

        for account in bank.accounts.values():
            data.append({
                "account_number": account.account_number,
                "owner_name": account.owner_name,
                "balance": account.balance
            })

        try:
            with open(filename, "w") as f:
                json.dump(data, f, indent=4)
        except OSError as e:
            raise IOError(f"Failed to save bank data to {filename}: {e}")

   



