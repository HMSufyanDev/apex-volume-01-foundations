# What Is a List?
# A list is a Python data structure that stores multiple values in a single variable.

countries = ["Pakistan", "Australia", "Canada", "UK", "USA"]

# Empty List
leads = []

# List of Strings
countries = ["Australia", "Canada", "UK"]

# List of Numbers
monthly_income = [500, 800, 1200, 1500]

# Mixed Data Types
mixed_data = ["Sufyan", 21, True, 500.0]

# List Indexing
leads = ["ABC Dental", "XYZ Clinic", "Smile Care"]

print(leads[0]) # ABC Dental
print(leads[1]) # XYZ Clinic

# Negative Indexing
leads = ["ABC Dental", "XYZ Clinic", "Smile Care"]
print(leads[-1]) # Smile Care

# IndexError
leads = ["ABC Dental", "XYZ Clinic", "Smile Care"]
print(leads[5]) # IndexError: list index out of range

# List Slicing
leads = ["A", "B", "C", "D", "E"]
# basic syntax: list[start:stop]
print(leads[0:3]) # ["A", "B", "C"]

# Shortcut Slicing
# From Beginning
leads[:3] # same as leads[0:3]

# From an Index to the End
leads[2:] # ["C", "D", "E"]

# Last Two Items
leads[-2:] # ["D", "E"]

# Membership Operators
# Using in
countries = ["Pakistan", "Australia", "Canada"]
print("Australia" in countries) # True

# Using not in
countries = ["Pakistan", "Australia", "Canada"]
print("USA" not in countries) # True


