import csv
import os

class FileHandler:
    """Reusable CSV file handler for reading and writing."""

    @staticmethod
    def initialize_csv(file_path, fieldnames):
        """Ensure file exists with header."""
        if not os.path.exists(file_path):
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
            with open(file_path, 'w', newline='', encoding='utf-8') as file:
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()

    @staticmethod
    def read_csv(file_path, fieldnames):
        """Read CSV and return list of dicts."""
        FileHandler.initialize_csv(file_path, fieldnames)
        data = []
        with open(file_path, 'r', newline='', encoding='utf-8') as file:
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
