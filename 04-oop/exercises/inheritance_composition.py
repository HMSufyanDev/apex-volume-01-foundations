# INHERITANCE AND SUPER()

class Person:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def introduce(self):
        return f"My name is {self.name}."


# Child class inheriting from Person using super()
class Client(Person):
    def __init__(self, name, email, company):
        super().__init__(name, email)
        self.company = company
        self.projects = [] 

    # Child-specific method
    def pay_invoice(self):
        print(f"{self.name} from {self.company} paid the invoice.")

    # Method overriding using super()
    def introduce(self):
        message = super().introduce()
        return f"{message} I am a client from {self.company}."

   
    def add_project(self, project):
        self.projects.append(project)

    def list_projects(self):
        print(f"Projects for {self.name}:")
        for project in self.projects:
            print(f"- {project.name}")

    def calculate_revenue(self):
        return sum(project.calculate_revenue() for project in self.projects)


class Employee(Person):
    def __init__(self, name, email, role):
        super().__init__(name, email)
        self.role = role

# COMPOSITION (CLIENT -> PROJECT -> INVOICE)

class Invoice:
    def __init__(self, amount):
        self.amount = amount
        self.status = "unpaid"

    def mark_as_paid(self):
        self.status = "paid"


class Project:
    def __init__(self, name, budget):
        self.name = name
        self.budget = budget
        self.invoices = []

    def add_invoice(self, invoice):
        self.invoices.append(invoice)

    def calculate_revenue(self):
        return sum(invoice.amount for invoice in self.invoices)



print("Testing Inheritance & Methods")
client1 = Client("Sarah Connor", "sarah@cyberdyne.com", "Cyberdyne")
print(client1.introduce())
client1.pay_invoice()

employee1 = Employee("John Doe", "john@example.com", "Developer")
print(f"Employee: {employee1.name}, Role: {employee1.role}")


print("\nTesting Composition (Projects & Invoices)")
# Create Projects
project1 = Project("Ecommerce Website", 5000)
project2 = Project("Mobile App", 8000)

# Create Invoices
invoice1 = Invoice(2500)
invoice2 = Invoice(2500)
invoice3 = Invoice(4000)

# Connect Project -> Invoices
project1.add_invoice(invoice1)
project1.add_invoice(invoice2)
project2.add_invoice(invoice3)

# Connect Client -> Projects
client1.add_project(project1)
client1.add_project(project2)


print("\nViewing Results")
# List all client projects
client1.list_projects()

# Calculate revenue
print(f"Project 1 Revenue: ${project1.calculate_revenue()}")
print(f"Project 2 Revenue: ${project2.calculate_revenue()}")
print(f"Total Client Revenue: ${client1.calculate_revenue()}")