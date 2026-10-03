def get_name(name: str) -> str:

    if not name:
        raise ValueError("Invalid Name: Name cannot be empty or blank.")
    
    return name

def validate_positive(value: float | int) -> float | int:

    if value < 0:
        raise ValueError("Invalid Value: Number must be positive.")
    
    return value

def validate_rarity(rarity: str) -> str:

    RARITY = {
        "Common",
        "Rare",
        "Epic",
        "Legendary"
    }

    if rarity.capitalize() not in RARITY:
        raise ValueError(f"Invalid Rarity:\n Choose: {RARITY}")

    return rarity
