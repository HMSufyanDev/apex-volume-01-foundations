# if statement
age: int = 22

if age >= 18:
    print("You are an adult.") # True

# else
age: int = 15

if age >= 18:
    print("You are an adult.")
else:
    print("You are under 18.") # You are under 18.

# elif
score: int = 85

if score >= 90:
    print("A")
elif score >= 80:
    print("B") # B
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")

# Order matters
score: int = 95

if score >= 60:
    print("D")
elif score >= 90:
    print("A")
# You might expect A.
# But Python sees:
# 95 >= 60, which is already True, so it prints D

# Nested conditions
age: int = 25
has_id: bool = True

if age >= 18:
    if has_id:
        print("Access granted.")
    else:
        print("ID required.")
else:
    print("You are under 18.")

# Truthy and falsy values
# Some values behave like False when used in a condition.
name: str = ""

if name:
    print("Name exists.")
else:
    print("Name is empty.") # This will run, because "" is falsy

# Common falsy values
False
None
0
0.0
""
[]
{}