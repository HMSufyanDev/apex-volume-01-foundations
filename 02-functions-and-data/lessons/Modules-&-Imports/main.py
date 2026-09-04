# In Python, a module is essentially a Python file that contains code you can use elsewhere.

import calculations

revenue = calculations.calculate_revenue(5, 500)

print(revenue) # 2500

# from x import y
# Instead of import calculations
from calculations import calculate_revenue

revenue = calculate_revenue(5, 300)
print(revenue) # 1500

# Multiple functions

from calculations import (
    calculate_revenue,
    calculate_total_expenses,
    calculate_net_income,
)


revenue = calculate_revenue(5, 500)

expenses = calculate_total_expenses(100, 50, 150,)

net_income = calculate_net_income(revenue, expenses,)

print(net_income)

# What is __name__?
# If you run a file directly: python main.py
# Python sets: __name__ == "__main__"
# But if another file imports it: import main
# then its __name__ is: main

# if __name__ == "__main__":
if __name__ == "__main__":
    print("Program started")
# It means: Only run this code when this file is executed directly.
# Example in calculations.py



# Standard Library
import math
print(math.sqrt(25)) # 5.0

import random
number = random.randint(1, 10)
print(number)

from datetime import datetime
now = datetime.now()
print(now)

import os
print(os.getcwd()) # Can interact with parts of the operating system.

import json
data = {
    "name": "Sufyan",
    "clients": 5,
}
json_data = json.dumps(data)
print(json_data) # {"name": "Sufyan", "clients": 5}