class Lead:

    def __init__(self, name, email, country, estimated_value):
        self.name = name
        self.email = email
        self.country = country
        self.estimated_value = estimated_value
        self.status = "New"

    def mark_contacted(self):
        self.status = "Contacted"

    def qualify(self):
        self.status = "Qualified"

    def is_high_value(self):
        return self.estimated_value >= 1000

    def convert_to_client(self):
        if self.status != "Qualified":
            return None

        from .client import Client

        return Client(
            self.name,
            self.email,
            self.country
        )

    def __str__(self):
        return f"{self.name} - {self.status} - ${self.estimated_value:.2f}"