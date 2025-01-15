from shift import Shift
import csv

class ShiftManager:

    def __init__(self, file_path='shifts.csv', list_of_shifts=None):
        self.file_path = file_path
        self.list_of_shifts = list_of_shifts if list_of_shifts is not None else []

    def write_shifts(self):
        try:
            with open(self.file_path, 'w', newline='') as csvfile:
                fieldnames = ['date', 'role', 'start_time', 'end_time']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                for shift in self.list_of_shifts:
                    writer.writerow(shift.to_dict())
            print(f"Shifts successfully saved to {self.file_path}")
        except Exception as e:
            print(f"Error writing to CSV: {e}")
    
    def read_shifts(self):
        """Corrected method with 'self' parameter"""
        try:
            with open(self.file_path, mode='r') as file:
                reader = csv.DictReader(file)
                self.list_of_shifts = [
                    Shift(row['date'], row['role'], row['start_time'], row['end_time'])
                    for row in reader
                ]
            print(f"Shifts successfully loaded from {self.file_path}")
        except FileNotFoundError:
            print(f"File '{self.file_path}' not found.")
        except Exception as e:
            print(f"Error reading from CSV: {e}")