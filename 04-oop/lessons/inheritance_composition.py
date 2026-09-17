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


# Composition
# Composition means an object contains or uses other objects.

class Client:

    def __init__(self, name):
        self.name = name
        self.projects = []

# Create Project
class Project:

    def __init__(self, name, budget):
        self.name = name
        self.budget = budget
        self.invoices = []

# Create Invoice
class Invoice:

    def __init__(self, amount):
        self.amount = amount
        self.status = "unpaid"

# Connecting Client → Project
client1 = Client("Sarah Connor")
project1 = Project("Ecommerce Website", 5000)
client1.projects.append(project1)

# Connecting Project → Invoice
invoice1 = Invoice(2500)
invoice2 = Invoice(2500)

project1.invoices.append(invoice1)
project1.invoices.append(invoice2)

# The complete relationship
client = Client("Sarah")
project1 = Project("Website", 5000)
project2 = Project("Mobile App", 8000)

invoice1 = Invoice(2500)
invoice2 = Invoice(2500)
invoice3 = Invoice(4000)

client.projects.append(project1)
client.projects.append(project2)

project1.invoices.append(invoice1)
project1.invoices.append(invoice2)

project2.invoices.append(invoice3)

# Let's make adding projects a method
class Client:

    def __init__(self, name):
        self.name = name
        self.projects = []

    def add_project(self, project):
        self.projects.append(project)

class Project:

    def __init__(self, name, budget):
        self.name = name
        self.budget = budget
        self.invoices = []

    def add_invoice(self, invoice):
        self.invoices.append(invoice)

client1.add_project(project1)
project1.add_invoice(invoice1)


# Listing Projects
class Client:

    def __init__(self, name):
        self.name = name
        self.projects = []

    def add_project(self, project):
        self.projects.append(project)

    def list_projects(self):
        for project in self.projects:
            print(project.name)


# Calculating project revenue
class Project:

    def __init__(self, name, budget):
        self.name = name
        self.budget = budget
        self.invoices = []

    def add_invoice(self, invoice):
        self.invoices.append(invoice)

    def calculate_revenue(self):
        return sum(invoice.amount for invoice in self.invoices)

# Calculating client revenue
class Client:

    def __init__(self, name):
        self.name = name
        self.projects = []

    def add_project(self, project):
        self.projects.append(project)

    def calculate_revenue(self):
        return sum(
            project.calculate_revenue()
            for project in self.projects
        )