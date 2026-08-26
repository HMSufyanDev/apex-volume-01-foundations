
# Python is case-sensitive.
# Data Types
profession: str = "Software Engineer" # String
print(profession)
age: int = 22 # Integer
print(age)
price: float = 99.99 # Float
print(price)
is_student: bool = False # Bool
print(is_student)
middle_name: str | None = None # This means: middle_name currently has no value.
print(middle_name)
#It's different from:
middle_name = "" # because an empty string is still a string.

# Or we can write:
a = 71 # identifies a as class <int> 
b = 88.44 # identifies b as class <float>
name = "sufyan" # identifies name as class <str>

# type()

name: str = "Sufyan"
age: int = 22
income: float = 5000.50
is_student: bool = False

print(type(name))
print(type(age))
print(type(income))
print(type(is_student))

# Type conversion

# Convert to string:
number: int = 100
text: str = str(number)

# Convert to integer:
price_text: str = "500"
price: int = int(price_text)

# Convert to a float:
price_text: str = "500.50"
price: float = float(price_text)

# Convert to a boolean:
value: int = 1
result: bool = bool(value)

print(result)
