# Exercise 1 — Safe Age Input
def get_valid_age() -> int:

    while True:
        get_input = input("Enter your age: ")
        
        try:
            age = float(get_input)
            if age < 0:
                print("Age cannot be negative.")
                continue
        
        except ValueError as e:
            print("Please enter a valid whole number.")
            continue

        return age
    
print(get_valid_age())


# Exercise 4 — Validation Range
def get_valid_percentage() -> float:
    while True:
        get_input = input("Enter percentage: ")

        try:
            percentage = float(get_input)
            if percentage < 0 or percentage > 100:
                print("Value should between 0 to 100")
                continue
        except ValueError:
            print("Enter a valid percentage")
            continue

        return percentage

print(get_valid_percentage())