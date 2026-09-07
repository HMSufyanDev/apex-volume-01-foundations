import validators

def get_client_count() -> int:
    client_count = int(input("How many clients do you have?: "))
    valid = validators.is_valid_client_count(client_count)
    while not valid:
        print("Error: Number of clients cannot be negative. Try again.")
        client_count = int(input("How many clients do you have?: "))
        valid = validators.is_valid_client_count(client_count)
    return client_count

def get_project_price() -> float:
    project_price = float(input("What is your average project value?: "))
    valid = validators.is_valid_price(project_price)
    while not valid:
        print("Error: Project value cannot be negative. Try again.")
        project_price = float(input("What is your average project value?: "))
        valid = validators.is_valid_price(project_price)
    return project_price

def get_platform_fee() -> float:
    platform_fee = float(input("What percentage does the platform charge?: "))
    valid = validators.is_valid_platform_fee(platform_fee)
    while not valid:
        print("Error: Platform fee must between 0 to 100. Try again.")
        platform_fee = float(input("What percentage does the platform charge?: "))
        valid = validators.is_valid_platform_fee(platform_fee)
    return platform_fee

def get_software_cost() -> float:
    software_cost = float(input("What is your software cost?: "))
    valid = validators.is_valid_software_cost(software_cost)
    while not valid:
        print("Error: Software cost cannot be negative. Try again.")
        software_cost = float(input("What is your software cost?: "))
        valid = validators.is_valid_software_cost(software_cost)
    return software_cost

def get_internet_cost() -> float:
    internet_cost = float(input("What is your internet cost?: "))
    valid = validators.is_valid_internet_cost(internet_cost)
    while not valid:
        print("Error: Internet cost cannot be negative. Try again.")
        internet_cost = float(input("What is your internet cost?: "))
        valid = validators.is_valid_internet_cost(internet_cost)
    return internet_cost

def get_other_expenses() -> float:
    other_expenses = float(input("What is your other expenses?: "))
    valid = validators.is_valid_other_expenses(other_expenses)
    while not valid:
        print("Error: Expenses cannot be negative. Try again.")
        other_expenses = float(input("What is your other expenses?: "))
        valid = validators.is_valid_other_expenses(other_expenses)
    return other_expenses

def get_exchange_rate() -> float:
    exchange_rate = float(input("What is the USD -> PKR exchange rate?: "))
    valid = validators.is_valid_exchange_rate(exchange_rate)
    while not valid:
        print("Error: Exchange rate must be greater than zero. Try again.")
        exchange_rate = float(input("What is the USD -> PKR exchange rate?: "))
        valid = validators.is_valid_exchange_rate(exchange_rate)
    return exchange_rate