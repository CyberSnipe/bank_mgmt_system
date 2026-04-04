import json
from pathlib import Path
from domain.bank_account import BankAccount

class AccountRepository:
    """Repository for managing multiple BankAccount objects in a single JSON file."""

    def __init__(self, filename: str):
        self.filename = filename
        self._ensure_file_exists()

    def _ensure_file_exists(self):
        """Create the JSON file if it does not exist."""
        path = Path(self.filename)
        if not path.exists():
            with open(self.filename, "w") as f:
                json.dump([], f)

    def _read_all(self) -> list[dict]:
        """Read and return all account dictionaries from the JSON file."""
        try:
            with open(self.filename, "r") as f:
                return json.load(f)
        except (OSError, json.JSONDecodeError):
            return []

    def _write_all(self, accounts: list[dict]) -> None:
        """Write the full list of account dictionaries to the JSON file."""
        try:
            with open(self.filename, "w") as f:
                json.dump(accounts, f, indent=4)
        except OSError as e:
            raise IOError(f"Failed to write accounts to {self.filename}: {e}")

    # ---------------------------------------------------------
    # CRUD OPERATIONS
    # ---------------------------------------------------------

    def add_account(self, account: BankAccount) -> None:
        """Add a new account to the JSON file."""
        accounts = self._read_all()

        # Prevent duplicates
        if any(a["account_number"] == account.account_number for a in accounts):
            raise ValueError(f"Account '{account.account_number}' already exists.")

        accounts.append({
            "account_number": account.account_number,
            "owner_name": account.owner_name,
            "balance": account.balance
        })

        self._write_all(accounts)

    def get_account(self, account_number: str) -> BankAccount | None:
        """Retrieve a BankAccount by account number."""
        accounts = self._read_all()

        for entry in accounts:
            if entry["account_number"] == account_number:
                return BankAccount(
                    account_number=entry["account_number"],
                    owner_name=entry["owner_name"],
                    balance=float(entry["balance"])
                )

        return None

    def update_account(self, account: BankAccount) -> None:
        """Update an existing account."""
        accounts = self._read_all()
        updated = False

        for entry in accounts:
            if entry["account_number"] == account.account_number:
                entry["owner_name"] = account.owner_name
                entry["balance"] = account.balance
                updated = True
                break

        if not updated:
            raise KeyError(f"Account '{account.account_number}' not found.")

        self._write_all(accounts)

    def delete_account(self, account_number: str) -> None:
        """Delete an account by account number."""
        accounts = self._read_all()
        new_accounts = [a for a in accounts if a["account_number"] != account_number]

        if len(new_accounts) == len(accounts):
            raise KeyError(f"Account '{account_number}' not found.")

        self._write_all(new_accounts)

    def list_accounts(self) -> list[BankAccount]:
        """Return all accounts as BankAccount objects."""
        accounts = self._read_all()
        return [
            BankAccount(
                account_number=a["account_number"],
                owner_name=a["owner_name"],
                balance=float(a["balance"])
            )
            for a in accounts
        ]

