try:
    value = float(input("Enter a number: "))
except ValueError:
    print("Please enter a valid number.")

'''
try: as: "Try to run this code."
And:
except ValueError: means: "If converting the value causes a ValueError, handle it instead of crashing."
'''

try:
    age = int(input("Enter your age: "))
    print(f"Your age is {age}")

except ValueError:
    print("Please enter a valid whole number.")

# ValueError
# A ValueError happens when a value has the correct general type of operation but an invalid value for that operation
# example: int("hello")

# while True for Input Validation
# Basic Validation Pattern
while True:
    raw_value = input("Enter a number: ")

    try:
        value = float(raw_value)
    except ValueError:
        print("Please enter a valid number.")
        continue

    break

# Finally
# The finally block in Python always executes before leaving the try statement, whether an exception occurred or not
try:
    file = open("data.txt", "r")
    # Do some operations
except FileNotFoundError:
    print("File not found!")
finally:
    file.close()  # ALWAYS runs, regardless of errors above