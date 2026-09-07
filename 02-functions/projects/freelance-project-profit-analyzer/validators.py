def get_project_name() -> str:
    while True:
        project_name = input("Enter Your Project Name: ").strip()
        if not project_name:
            print("Project name cannot be empty, try again!")
            continue
        
        return project_name

def get_non_negative_float(command) -> float:
    while True:

        raw_input = input(command).strip()
        if not raw_input:
            print("Error: Input cannot be empty. Please enter a number.")
            continue
        elif " " in raw_input:
            print("Spaces not allowed!, try again")
            continue

        try:
            non_negative_float = float(raw_input)
            
            if non_negative_float < 0:
                print("The value cannot be negative, try again")
                continue
            return non_negative_float
        
        except ValueError:
                print("Error: The value should be a number.")
                continue

def get_positive_int(command) -> int:
    while True:

        raw_input = input(command).strip()
        if not raw_input:
            print("Error: Input cannot be empty. Please enter a number.")
            continue
        elif " " in raw_input:
            print("Spaces not allowed!, try again")
            continue

        try:
            positive_int = int(raw_input)
            if positive_int <= 0:
                print("The value must be greater than 0, try again")
                continue
            return positive_int
        except ValueError:
                print("Error: The value should be a number.")
                continue

def get_valid_percentage() -> float:
    while True:

        raw_input = input("Enter platform percentage: ").strip()
        if not raw_input:
            print("Error: Input cannot be empty. Please enter a percentage.")
            continue
        elif " " in raw_input:
            print("Spaces not allowed!, try again")
            continue

        try:
            percentage = float(raw_input)
            if not  0 <= percentage <= 100:
                print("The percentage must between 0 to 100, try again!")
                continue
            return percentage / 100
        except ValueError:
                print("Error: The percentage should be a number.")
                continue
    