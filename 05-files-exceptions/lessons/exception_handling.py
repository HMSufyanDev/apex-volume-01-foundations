# try
# Python, try this code. I know something could go wrong here."
# try:
#     age = int(input("Enter your age: "))

# try + except
try:
    age = int(input("Enter your age: "))

except ValueError:
    print("Please enter a valid number.")

# Only Handles the Exceptions You Specify
try:
    number = int(input("Number: "))
except ValueError:
    print("Invalid number.")
# This catches: ValueError

# Multiple Exceptions
try:
    number = int(input("Enter a number: "))
    result = 100 / number

except ValueError:
    print("Please enter a valid number.")

except ZeroDivisionError:
    print("You cannot divide by zero.")

# except ... as error
try:
    number = int("hello")

except ValueError as error:
    print(error)

# else
# else runs only when the try block succeeds without an exception.
try:
    number = int(input("Enter a number: "))

except ValueError:
    print("Invalid number.")

else:
    print("Number accepted:", number)

# finally
# finally runs no matter whether the operation succeeds or fails.
try:
    number = int(input("Number: "))

except ValueError:
    print("Invalid number.")

finally:
    print("This always runs.")

# Full try Structure
# try:
#     risky_operation()

# except SomeError:
#     handle_error()

# else:
#     handle_success()

# finally:
#     cleanup()

# Raising Your Own Exception
# But sometimes we want to tell Python that something is invalid.
# raise
amount = -500
if amount < 0:
    raise ValueError("Amount cannot be negative.")

# Custom Exceptions
# For example lead not found
class LeadNotFoundError(Exception):
    pass
# It behaves like an exception because it comes from Exception.
lead = None
if lead is None:
    raise LeadNotFoundError("Lead was not found.")

# except Exception as error:
#     print(error)
# It can be useful at a top-level application boundary, for logging or preventing a CLI application from crashing unexpectedly.

# Handle Unexpected Data Explicitly
# if not isinstance(data, dict):
#     raise ValueError("Expected JSON object.")