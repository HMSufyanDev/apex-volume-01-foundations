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
invoice.amount = -100 # ValueError: Amount cannot be negative

