import random
import time
import csv
from datetime import datetime

def generate_mock_data(file_name="health_data.csv", interval=2):
    """
    Simulates real-time health data generation.
    """
    # Initialize the CSV file with headers
    with open(file_name, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["timestamp", "heart_rate", "steps", "spo2", "calories"])  # Header

    while True:
        # Append a new row with random data
        with open(file_name, mode="a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([
                datetime.now().strftime("%Y-%m-%d %H:%M:%S"),  # Current timestamp
                random.randint(60, 180),  # Heart rate
                random.randint(0, 20000),  # Steps
                random.randint(90, 100),  # SpO₂
                random.randint(1500, 3000)  # Calories burned
            ])
        print(f"New data row added at {datetime.now().strftime('%H:%M:%S')}")
        time.sleep(interval)

if __name__ == "__main__":
    generate_mock_data()
