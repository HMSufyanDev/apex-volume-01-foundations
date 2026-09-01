def is_valid_client_count(client_count: int) -> bool:
    return client_count >= 0

def is_valid_price(price: float) -> bool:
    return price >= 0

def is_valid_platform_fee(platform_fee: float) -> bool:
    return platform_fee >= 0 and platform_fee <= 100

def is_valid_software_cost(software_cost: float) -> bool:
    return software_cost >= 0

def is_valid_internet_cost(internet_cost: float) -> bool:
    return internet_cost >= 0

def is_valid_other_expenses(other_expenses: float) -> bool:
    return other_expenses >= 0

def is_valid_exchange_rate(other_expenses: float) -> bool:
    return other_expenses > 0
