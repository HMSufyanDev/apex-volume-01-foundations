# __init__
# Default values inside __init__

class Lead:

    def __init__(self, name, email, estimated_value):
        self.name = name
        self.email = email
        self.estimated_value = estimated_value
        self.status = "new"

# Methods
# A function defined inside a class is called a method.

class Lead:

    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"Lead: {self.name}")

lead1 = Lead("Sarah")
lead1.introduce() # Lead: Sarah


# Instance methods
class Lead:
    def introduce(self):
        print("I am a lead")

lead1 = Lead()
lead1.introduce()


# Methods can modify object state
class Lead:

    def __init__(self, name):
        self.name = name
        self.status = "new"

    def mark_contacted(self):
        self.status = "contacted"

lead1 = Lead("Sarah")
print(lead1.status) # new

lead1.mark_contacted()
print(lead1.status) # contacted

# Methods with parameters
class Lead:

    def __init__(self, name):
        self.name = name
        self.status = "new"

    def change_status(self, new_status):
        self.status = new_status

lead1 = Lead("Sarah")
lead1.change_status("qualified")
print(lead1.status) # qualified


# Methods can return values
class Project:

    def __init__(self, budget, expenses):
        self.budget = budget
        self.expenses = expenses

    def calculate_profit(self):
        return self.budget - self.expenses


project1 = Project(5000, 1200)
profit = project1.calculate_profit()

print(profit) # 3800

# class attributes
class Lead:

    source = "Website"

# source is a class attribute.
# It belongs to the class itself and is shared as a default value by instances.

# Methods can call other methods using self
class Lead:

    def __init__(self, name):
        self.name = name
        self.status = "new"

    def mark_contacted(self):
        self.status = "contacted"

    def is_active(self):
        return self._get_status() != "closed"

    def _get_status(self):
        return self.status

lead1 = Lead("Sarah")
print(lead1.is_active())