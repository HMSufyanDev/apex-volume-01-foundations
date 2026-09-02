# --------- datetime -------------
'''
The datetime module helps you work with:
Current date
Current time
Specific dates
Time differences
Formatting dates
'''

import datetime
current_time = datetime.datetime.now()

print(current_time)

# OR, I can write
from datetime import datetime
now = datetime.now()
print(now)

# Getting only the date
from datetime import date
today = date.today()
print(today)

# Creating a specific date
from datetime import datetime
birthday = datetime(2000, 5, 10)
print(birthday)

# Formatting dates
from datetime import datetime
now = datetime.now()
formatted_date = now.strftime("%d-%m-%Y") # 02-09-2026
print(formatted_date)
# OR
formatted_date = now.strftime("%B %d, %Y")
print(formatted_date) # September 02, 2026


# ----------- math ----------
# Square root
import math
result = math.sqrt(25)
print(result) # 5.0

# Power
result = math.pow(2, 3)
print(result) # 8.0

# Rounding up
number = math.ceil(4.2)
print(number) # 5

# Rounding down
number = math.floor(4.8)
print(number) # 4


# Pi
print(math.pi)


# ------------- random ---------------
# Random integer
import random
number = random.randint(1, 10)
print(number)

# Random choice from a list
platforms = ["Upwork", "Fiverr", "LinkedIn", "Direct Outreach",]
selected_platform = random.choice(platforms)
print(selected_platform)

# Shuffle a list
clients = ["Client A","Client B", "Client C", "Client D",]
random.shuffle(clients)
print(clients)
# shuffle() changes the original list.

# --------------- statistics: Working with Numerical Data ----------------
# Mean (Average)
import statistics
monthly_income = [
    1000,
    1500,
    2000,
    1800,
    2500,
]
average_income = statistics.mean(monthly_income)
print(average_income) # 1760

# Median
median_income = statistics.median(monthly_income)
print(median_income)

# Maximum and minimum?
# i actually don't need statistics for those.
max(monthly_income)
min(monthly_income)

# Standard deviation
standard_deviation = statistics.stdev(monthly_income)
print(standard_deviation)

# ---------------- pathlib -----------
# Creating a Path
from pathlib import Path
current_path = Path(".") # The dot . means the current directory.
print(current_path)

# Getting the current working directory
current_path = Path.cwd()
print(current_path)

# Checking if a file exists
file_path = Path("data.txt")

if file_path.exists():
    print("File exists.")
else:
    print("File does not exist.")

# Creating a folder
folder = Path("reports")
folder.mkdir(exist_ok=True)

# Creating a file path
folder = Path("reports")
file_path = folder / "income_report.txt"
print(file_path)