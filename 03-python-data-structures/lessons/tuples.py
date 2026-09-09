# A tuple is a collection of multiple values, similar to a list.
countries = ("Australia", "Canada", "UK")

print(countries[0])
print(countries[-1])
print(countries[:2])
print(len(countries))

# Tuple Immutability
# countries = ("Australia", "Canada", "UK")
# countries[0] = "USA" TypeError: 'tuple' object does not support item assignment

# Tuple Indexing
user = ("Sufyan", 21, "Pakistan")
print(user[0]) # Sufyan

# Tuple Slicing
user = ("Sufyan", 21, "Pakistan", "AI Engineer")
print(user[:2]) # ('Sufyan', 21)

# Tuple Packing
user = "Sufyan", 21, "Pakistan"
print(user)
print(type(user))
# ('Sufyan', 21, 'Pakistan')
# <class 'tuple'>

# Tuple Unpacking
name, age, country = user
print(name) # Sufyan
print(age) # 21
print(country) # Pakistan

# Note: Normally, the number of variables must match the number of values

# name, age = user
# ValueError: too many values to unpack

# Extended Unpacking with *
user = ("Sufyan", 21, "Pakistan", "AI Software Engineer")
name, *details = user
print(name) # Sufyan
print(details) # [21, 'Pakistan', 'AI Software Engineer']
# You Can Also Capture the Middle
numbers = (10, 20, 30, 40, 50)
first, *middle, last = numbers
print(first)
print(middle)
print(last)

