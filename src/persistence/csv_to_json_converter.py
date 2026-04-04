import csv
import json
from pathlib import Path

class CSVtoJSONConverter:
    """Utility class for converting CSV files to JSON format."""

    @staticmethod
    def convert(csv_filename: str, json_filename: str) -> None:
        """Convert a CSV file into a JSON file."""
        csv_path = Path(csv_filename)

        if not csv_path.exists():
            raise FileNotFoundError(f"CSV file '{csv_filename}' does not exist.")

        rows = []

        try:
            with open(csv_filename, "r", newline="") as csvfile:
                reader = csv.DictReader(csvfile)

                for row in reader:
                    # Convert numeric fields if needed
                    if "balance" in row:
                        try:
                            row["balance"] = float(row["balance"])
                        except ValueError:
                            row["balance"] = None

                    rows.append(row)

            with open(json_filename, "w") as jsonfile:
                json.dump(rows, jsonfile, indent=4)

        except OSError as e:
            raise IOError(f"Failed to convert CSV to JSON: {e}")

