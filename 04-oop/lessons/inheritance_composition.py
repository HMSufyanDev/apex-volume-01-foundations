# Inheritance allows us to say: Client and Employee are both types of Person.

# Parent class
class Person:

    def __init__(self, name, email):
        self.name = name
        self.email = email


# Child class
class Client(Person):
    pass
# Client inherits from Person.

# Creating a Client
# Because Client inherits from Person:
client = Client("Sarah", "sarah@example.com")
print(client.name)
print(client.email)

# Another child
class Employee(Person):
    pass
client = Client("Sarah", "sarah@example.com")
employee = Employee("John", "john@example.com")

# Adding child-specific attributes
class Client(Person):

    def __init__(self, name, email, company):
        self.name = name
        self.email = email
        self.company = company
# We're repeating:
# That's where super() comes in.

# super()
class Client(Person):

    def __init__(self, name, email, company):
        super().__init__(name, email)
        self.company = company

# Example
class Person:

    def __init__(self, name, email):
        self.name = name
        self.email = email


class Client(Person):

    def __init__(self, name, email, company):
        super().__init__(name, email)
        self.company = company

client = Client(
    "Sarah Connor",
    "sarah@example.com",
    "Cyberdyne"
)


# Method inheritance
class Person:

    def introduce(self):
        print(f"My name is sufyan")


class Client(Person):
    pass

client = Client()
client.introduce()

# Child-specific methods
class Client(Person):

    def pay_invoice(self):
        print(f"sufyan paid the invoice.")

client = Client()
client.pay_invoice()

# Method overriding
class Person:

    def introduce(self):
        return "I am a person."

class Client(Person):

    def introduce(self):
        return "I am a client."

client = Client()
print(client.introduce()) # I am a client.

# super() with overridden methods
class Person:

    def introduce(self):
        return "My name is Sufyan."


class Client(Person):

    def introduce(self):
        message = super().introduce()
        return f"{message} I am a client."

client = Client()
print(client.introduce())