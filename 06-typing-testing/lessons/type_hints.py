# Type hints are labels that tell us what kind of data a function expects and what kind of data it will give back.

# Types
name = "Sufyan"
age = 21
price = 1500.50
is_paid = True

print(type(name))
print(type(age))
print(type(price))
print(type(is_paid))

# str    = text
# int    = whole number
# float  = decimal number
# bool   = True / False


# type hint
def calculate_total(price: float, tax: float) -> float:
    return price + tax
# price should be a float
# tax should be a float
# the function returns a float

# Type hints don't force Python
def calculate_total(price: float, tax: float) -> float:
    return price + tax
# calculate_total("100", "20") No error
# Type hints are hints, not strict locks.


# Type hints for strings
def greet(name: str) -> str:
    return f"Hello {name}"

# Type hints for integers
def calculate_age(year: int) -> int:
    return 2026 - year

# Type hints for booleans
def is_high_value(amount: float) -> bool:
    return amount >= 1000


# collections

names: list[str] = ["Sufyan", "Ali", "Ahmed"]
# Means: A list containing strings.

ages: list[int] = [18, 20, 25]
# A list containing integers.

prices: list[float] = [100.5, 250.0, 999.99]
# A list containing floats.

# Function returning a list
def get_names() -> list[str]:
    return ["Sufyan", "Ali", "Ahmed"]

# Dictionaries
lead: dict[str, str] = {
    "name": "Sarah",
    "country": "USA"
}
# Means: Dictionary with string keys and string values.

prices: dict[str, int] = {
    "website": 5000,
    "app": 10000,
    "seo": 3000
}

lead = {
    "name": "Sarah Connor",
    "country": "USA",
    "email": "sarah@example.com",
    "status": "new",
    "estimated_value": 4500.0
}
# The values are not all the same type. So,
dict[str, object]


# tuple[str, int]
person = ("Sufyan", 21)
person: tuple[str, int] = ("Sufyan", 21)
# A tuple where the first item is a string and the second item is an integer.


# set[str]
countries: set[str] = {
    "Pakistan",
    "USA",
    "UK"
}

# None
# It basically means: "There is no value."
def mark_paid(self) -> None:
# why? Because the function changes something but doesn't return anything.

# Lead | None
def find_lead(email: str) -> Lead | None: # type: ignore
    pass
"Give me an email string. I might give you a Lead, or I might give you None."

# Why not just say Lead?
def find_lead(email: str) -> Lead: # type: ignore
    pass
"This function ALWAYS returns a Lead."
# It tells the person reading your code: "Be careful. You might get a Lead, but you might get None."

# Type aliases
LeadData = dict[str, object]
# Instead of repeatedly writing: dict[str, object]
# Then,
def find_lead(email: str) -> LeadData | None:
    pass


# Type Hint Cheat Sheet
# Type hint	        Meaning
# str	            text
# int	            whole number
# float	            decimal number
# bool	            True / False
# None	            no value
# list[str]	        list of strings
# list[int]	        list of integers
# dict[str, str]	string → string
# dict[str, int]	string → integer
# tuple[str, int]	string + integer
# set[str]	        set of strings
# Lead | None	    Lead or None
# str | None	    string or None