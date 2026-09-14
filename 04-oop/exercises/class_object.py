class Lead:
    pass

lead1 = Lead()
lead2 = Lead()
lead3 = Lead()

lead1.name = "Sarah Connor"
lead1.email = "sarah@example.com"
lead1.country = "United States"
lead1.estimated_value = 4500.0
lead1.status = "New"

lead2.name = "Alex Martin"
lead2.email = "alex@example.com"
lead2.country = "France"
lead2.estimated_value = 300.0
lead2.status = "Contacted"

print(lead1.name)
print(lead1.email)
print(lead1.country)
print(lead1.estimated_value)
print(lead1.status)

lead1.status = "Qualified"
print(lead1.status)


class Lead:
    def __init__(self, name, email, country, estimated_value, status):
        self.name = name
        self.email = email
        self.country = country
        self.estimated_value = estimated_value
        self.status = status


lead1 = Lead("Sarah", "sarah@example.com", "United States", 4500.0, "New")
print(lead1.name)
lead1.name = "sufyan"
print(lead1.name)