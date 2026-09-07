# Exercise 1 — Daily Report Date
from datetime import datetime
now = datetime.now()
format_now = now.strftime("%d-%m-%y")
print(f"Report generated on: {format_now}")


# Exercise 2 — Random Client Selector
import random
clients = [
    "Ali",
    "Ahmed",
    "Sara",
    "John",
    "Emma",
]

random_client = random.choice(clients)
print(f"Today's selected client: {random_client}")


# Exercise 3 — Income Statistics
import statistics
monthly_income = [
    1000,
    1500,
    2000,
    1800,
    2500,
]

print(f"Average income: {statistics.mean(monthly_income)}")
print(f"Median income: {statistics.median(monthly_income)}")
print(f"Standard deviation: {statistics.stdev(monthly_income)}")


# Exercise 4 — Math Practice
import math

print(f"{math.sqrt(144)}")
print(f"{math.ceil(8.7)}")
print(f"{math.floor(8.7)}")
print(f"{math.pi}")

# Exercise 5 — Reports Folder
from pathlib import Path
current_directory = Path.cwd()
print(f"Current working directory: {current_directory}")

folder = Path("reports")
folder.mkdir(exist_ok=True)

if folder.exists():
    print("Folder exists")
else:
    print("Folder not exist")

