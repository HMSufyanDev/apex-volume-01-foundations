class Lead:

    source = "Website"

    def __init__(self, name, email, estimated_value):
        self.name = name
        self.email = email
        self.estimated_value = estimated_value
        self.status = "new"

    def mark_contacted(self):
        self.status = "contacted"

    def qualify(self):
        self.status = "qualified"


class Client:

    def __init__(self, name, company, email, project_value):
        self.name = name
        self.company = company
        self.email = email
        self.project_value = project_value
        self.status = "active"

    def close_client(self):
        self.status = "closed"

    def update_value(self, new_value):
        self.project_value = new_value


class Project:

    def __init__(self, name, budget, hours):
        self.name = name
        self.budget = budget
        self.hours = hours
        self.status = "active"

    def calculate_hourly_rate(self):
        return self.budget / self.hours

    def complete(self):
        self.status = "completed"


class Invoice:

    def __init__(self, client_name, amount):
        self.client_name = client_name
        self.amount = amount
        self.status = "unpaid"

    def mark_paid(self):
        self.status = "paid"

    def get_status(self):
        return self.status


# Freelance Client Tracker
class Client:

    def __init__(self, name, company, email, project_value):
        self.name = name
        self.company = company
        self.email = email
        self.project_value = project_value
        self.status = "active"

    def close_client(self):
        self.status = "closed"

    def update_value(self, new_value):
            self.project_value = new_value

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Company: {self.company}")
        print(f"Email: {self.email}")
        print(f"Project Value: {self.project_value}")
        print(f"Status: {self.status}")

client1 = Client("Sufyan", "Apex Solutions", "sufyan@gmail.com", 14500.0)
client1.display_info()
client1.update_value(12400.0)
client1.close_client()
client1.display_info()
        