import csv
import os

class FileHandler:
    """Reusable CSV file handler for read/write operations."""

    @staticmethod
    def initialize_csv(file_path, fieldnames):
        """Create CSV with header if it doesn't exist."""
        if not os.path.exists(file_path):
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
            with open(file_path, 'w', newline='', encoding='utf-8') as file:
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()

    @staticmethod
    def read_csv(file_path, fieldnames):
        """Read data from CSV and return list of dictionaries."""
        FileHandler.initialize_csv(file_path, fieldnames)
        data = []
        with open(file_path, 'r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                data.append(row)
        return data

    @staticmethod
    def write_csv(file_path, fieldnames, data_list):
        """Write list of dictionaries to CSV."""
        FileHandler.initialize_csv(file_path, fieldnames)
        with open(file_path, 'w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for data in data_list:
                writer.writerow(data)
