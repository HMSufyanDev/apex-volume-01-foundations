# A class is a blueprint for creating objects.
class Lead:
    pass

# An object is an actual instance of a class.
lead1 = Lead()
lead2 = Lead()
lead3 = Lead()


class Lead:
    pass
lead1 = Lead()
lead1.name = "Sarah Connor"
lead1.email = "sarah@example.com"
lead1.country = "United States"
lead1.estimated_value = 4500.0
lead1.status = "New"

# Accessing attributes
print(lead1.name)
print(lead1.email)
print(lead1.country)
print(lead1.estimated_value)
print(lead1.status)

# Modifying attributes
lead1.status = "New"
lead1.status = "Qualified"

# self
class Lead:

    def __init__(self, name, email, country, estimated_value, status):
        self.name = name
        self.email = email
        self.country = country
        self.estimated_value = estimated_value
        self.status = status

lead1 = Lead(
    "Sarah Connor",
    "sarah@example.com",
    "United States",
    4500.0,
    "New"
)
# self refers to the current object.
# lead1 = Lead("Sarah", ...) Inside the class: self.name = name
# is effectively saying: lead1.name = "Sarah"

# Why do we need self?
# Because Python needs to know which object's data we're talking about.

# __init__
# def __init__(self, name, email, country, estimated_value, status):


lead2 = Lead(
    "Alex Martin",
    "alex@example.com",
    "France",
    3000.0,
    "Contacted"
)
print(lead1.name) # Sarah Connor
print(lead2.name) # Alex Martin

