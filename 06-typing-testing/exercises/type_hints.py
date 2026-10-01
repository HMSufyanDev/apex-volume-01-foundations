def greet(name: str) -> str:
    return f"Hello {name}"


def calculate_total(price: float, tax: float) -> float:
    return price + tax


def is_high_value(amount: float) -> bool:
    return amount >= 1000


def get_names() -> list[str]:
    return ["Sufyan", "Ali", "Ahmed"]

print(greet("Sufyan"))

print(calculate_total(1000.0, 150.0))

print(is_high_value(5000.0))

print(get_names())