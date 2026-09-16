# Encapsulation means controlling how an object's internal data can be accessed or changed.
# It means, Don't allow invalid or inappropriate changes.

# Public attributes
class Lead:

    def __init__(self, name, email):
        self.name = name
        self.email = email

# _protected convention
class Invoice:

    def __init__(self, amount):
        self._amount = amount

# __private and name mangling
class Invoice:

    def __init__(self, amount):
        self.__amount = amount

# Getters and setters
# invoice._amount We don't want people directly modifying it.
# get amount
# set amount

# @property
class Invoice:

    def __init__(self, amount):
        self._amount = amount

    @property
    def amount(self):
        return self._amount
invoice = Invoice(5000)
print(invoice.amount) # 5000
# @property lets a method behave like an attribute when accessed.

# the power appears when we add validation.
class Invoice:

    def __init__(self, amount):
        self.amount = amount

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        if value < 0:
            raise ValueError("Amount cannot be negative")

        self._amount = value
invoice = Invoice(5000)
# invoice.amount = -100 # ValueError: Amount cannot be negative

# Dunder Methods
# __init__ These are called dunder methods.

# __str__
class Lead:

    def __init__(self, name, status):
        self.name = name
        self.status = status

lead = Lead("Sarah", "new")
print(lead) # <__main__.Lead object at 0x000001...>

class Lead:

    def __init__(self, name, status):
        self.name = name
        self.status = status

    def __str__(self):
        return f"{self.name} - {self.status}"
    
lead = Lead("Sarah", "new")
print(lead) # Sarah - new
# When I write: print(lead)
# Python basically asks:
# "How should I turn this object into a human-readable string?"
# __str__() answers that question.

class Lead:

    def __init__(self, name, email, country, estimated_value, status):
        self.name = name
        self.email = email
        self.country = country
        self.estimated_value = estimated_value
        self.status = status

    def __str__(self):
        return (
            f"Lead: {self.name} | "
            f"Country: {self.country} | "
            f"Status: {self.status} | "
            f"Value: ${self.estimated_value}"
        )

lead = Lead(
    "Sarah Connor",
    "sarah@example.com",
    "United States",
    4500,
    "new"
)

print(lead) # Lead: Sarah Connor | Country: United States | Status: new | Value: $4500

# __repr__
# Developer/debugging representation.
class Lead:

    def __init__(self, name, status):
        self.name = name
        self.status = status

    def __str__(self):
        return f"{self.name} ({self.status})"

    def __repr__(self):
        return f"Lead(name={self.name!r}, status={self.status!r})"

lead = Lead("Sarah", "new")
print(lead) # Sarah (new)
print(repr(lead)) # Lead(name='Sarah', status='new')

# If the objects have a useful __repr__, seeing the list becomes much more informative.
# Imagine I'm debugging:
leads = [
    Lead("Sarah", "new"),
    Lead("Alex", "contacted")
]
for lead in leads:
    print(repr(lead))
# Lead(name='Sarah', status='new')
# Lead(name='Alex', status='contacted')

# __len__
class Project:

    def __init__(self, name, tasks):
        self.name = name
        self.tasks = tasks

    def __len__(self):
        return len(self.tasks)

project = Project(
    "Ecommerce Website",
    ["Homepage", "Login", "Cart", "Checkout"]
)
print(len(project)) # 4

# __eq__
class Lead:

    def __init__(self, email):
        self.email = email

    def __eq__(self, other):
        return self.email == other.email

lead1 = Lead("sarah@example.com")
lead2 = Lead("sarah@example.com")
# Without defining equality behavior, they aren't automatically considered equal merely because their emails match.

print(lead1 == lead2) # True
# Dunder methods let my objects participate naturally in Python's built-in operations.


# Dataclasses
# it can make classes dramatically shorter.
# Import dataclass
from dataclasses import dataclass
@dataclass
class Lead:
    name: str
    email: str
    country: str
    estimated_value: float
    status: str = "new"

# No manual __init__.
# Type annotations
name: str
email: str
country: str
estimated_value: float
status: str


@dataclass
class Lead:
    name: str
    email: str
    country: str
    estimated_value: float
    status: str = "new"

lead = Lead(
    "Sarah Connor",
    "sarah@example.com",
    "United States",
    4500
)
# The dataclass automatically provides the constructor.
