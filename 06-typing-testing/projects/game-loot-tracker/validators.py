def get_name(name: str) -> str:

    if not name:
        raise ValueError("Invalid Name: Name cannot be empty or blank.")
    
    return name

