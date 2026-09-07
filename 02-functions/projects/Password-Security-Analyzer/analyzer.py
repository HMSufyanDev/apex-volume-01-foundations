
def has_number(password) -> bool:
    has_numbers = any(char.isdigit() for char in password)
    return has_numbers

def has_uppercase(password) -> bool:
    has_uppercases = any(char.isupper() for char in password)
    return has_uppercases

def has_lowercase(password) -> bool:
    has_lowercases = any(char.islower() for char in password)
    return has_lowercases

def has_special_character(password) -> bool:
    has_special = any(not char.isalnum() and not char.isspace() for char in password)
    return has_special

def get_password_length(password) -> int:
    password_length = len(password)
    return password_length