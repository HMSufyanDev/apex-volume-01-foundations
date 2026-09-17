# Invoice + property
class Invoice:

    def __init__(self, amount):
        self._amount = amount
        self.status = "Unpaid"

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        if value < 0:
            raise ValueError("Error: Value cannot be negative!")

        self._amount = value

    def mark_paid(self):
        self.status = "Paid"

    def is_paid(self):
        return self.status == "Paid"


invoice = Invoice(5000)

print(invoice.amount)
print(invoice.is_paid())
invoice.mark_paid()
print(invoice.is_paid())
# invoice.amount = -500 # Raise ValueError
invoice.amount = 500
print(invoice.amount)

# Lead + __str__
class Lead:
    def __init__(self, name, status):
        self.name = name
        self.status = status

    def __str__(self):
        return f"Name: {self.name} | Status: {self.status}"

lead = Lead("Sufyan", "New")
print(lead)

# Project + __len__
class Project:
    def __init__(self, name, tasks):
        self.name = name
        self.tasks = tasks

    def __len__(self):
        return len(self.tasks)

proj = Project("Ecom website", ["navbar", "hero", "sidebar", "animations"])
print(len(proj))

# Lead + __eq__
class Lead:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __eq__(self, other):
        return (
            self.email == other.email
        )

lead1 = Lead("Sufyan", "sufyan@gmail.com")
lead2 = Lead("other", "sufyan@gmail.com")

print(lead1 == lead2)

# Dataclass
from dataclasses import dataclass
@dataclass
class Lead:
    name: str
    email: str
    country: str
    estimated_value: float
    status = "new"

    def mark_contacted(self):
        self.status = "contacted"

    def is_high_value(self):
        if self.estimated_value > 1000:
            return True
        return False

lead1 = Lead("sufyan", "sufyan@gmail", "pakistan", 3000.0)
print(lead1.name, lead1.email, lead1.country, lead1.status)
lead1.mark_contacted()
print(lead1.status)
print(lead1.is_high_value())
lead1.estimated_value = 500.0
print(lead1.is_high_value())