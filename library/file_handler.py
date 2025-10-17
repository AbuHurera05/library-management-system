import csv
import os

class FileHandler:
    """Reusable CSV file handler for reading and writing."""

    @staticmethod
    def initialize_csv(file_path, fieldnames=None):
        """Ensure file exists with header."""
        # Make sure folder exists
        if not os.path.exists(file_path):
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
            # If fieldnames not provided, create empty file
            with open(file_path, 'w', newline='', encoding='utf-8') as file:
                if fieldnames:
                    writer = csv.DictWriter(file, fieldnames=fieldnames)
                    writer.writeheader()

    @staticmethod
    def read_csv(file_path, fieldnames=None):
        """Read CSV and return list of dicts."""
        FileHandler.initialize_csv(file_path, fieldnames)
        data = []
        with open(file_path, 'r', newline='', encoding='utf-8') as file:
            # Automatically read headers if not provided
            if fieldnames:
                reader = csv.DictReader(file, fieldnames=fieldnames)
                next(reader, None)  # skip header row if given manually
            else:
                reader = csv.DictReader(file)

            for row in reader:
                data.append(row)
        return data

    @staticmethod
    def write_csv(file_path, fieldnames, data_list):
        """Write list of dicts to CSV."""
        FileHandler.initialize_csv(file_path, fieldnames)
        with open(file_path, 'w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data_list)
