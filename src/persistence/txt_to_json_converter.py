import json
from pathlib import Path

class TXTtoJSONConverter:
    """Convert .txt files into JSON format."""

    @staticmethod
    def convert(txt_filename: str, json_filename: str) -> None:
        txt_path = Path(txt_filename)

        if not txt_path.exists():
            raise FileNotFoundError(f"TXT file '{txt_filename}' does not exist.")

        accounts = []

        try:
            with open(txt_filename, "r") as f:
                for line in f:
                    parts = line.strip().split(",")

                    if len(parts) != 3:
                        continue  # skip malformed lines

                    account_number, owner_name, balance = parts

                    accounts.append({
                        "account_number": account_number,
                        "owner_name": owner_name,
                        "balance": float(balance)
                    })

            with open(json_filename, "w") as jf:
                json.dump(accounts, jf, indent=4)

        except OSError as e:
            raise IOError(f"Failed to convert TXT to JSON: {e}")

