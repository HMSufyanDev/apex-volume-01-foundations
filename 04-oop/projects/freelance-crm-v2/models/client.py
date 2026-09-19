class Client:
    
    def __init__(self, name, email, country):
        self.name = name
        self.email = email
        self.country = country
        self.projects = []

    def add_project(self, project):
        self.projects.append(project)

    def get_projects(self):
        return self.projects

    def get_total_revenue(self):
        return sum(
            project.get_total_invoiced()
            for project in self.projects
        )

    def get_paid_revenue(self):
        return sum(
            project.get_paid_revenue()
            for project in self.projects
        )

    def get_outstanding_revenue(self):
        return sum(
            project.get_outstanding()
            for project in self.projects
        )

    def get_history(self):
        return {
            "client": self.name,
            "projects": self.projects,
            "total_invoiced": self.get_total_revenue(),
            "paid_revenue": self.get_paid_revenue(),
            "outstanding_revenue": self.get_outstanding_revenue()
        }

    def __str__(self):
        return f"{self.name} - {self.email}"