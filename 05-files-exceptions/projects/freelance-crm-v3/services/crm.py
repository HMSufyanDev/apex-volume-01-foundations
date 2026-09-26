from models import Project, Invoice

class CRMService:

    def __init__(self):
        self.leads = []
        self.clients = []

    # -------------------------
    # Lead Management
    # -------------------------

    def add_lead(self, lead):
        self.leads.append(lead)

    def get_leads(self):
        return self.leads

    def search_lead(self, query):
        query = query.lower()

        return [
            lead
            for lead in self.leads
            if query in lead.name.lower()
            or query in lead.email.lower()
        ]

    def update_lead_status(self, lead, status):
        if status == "Contacted":
            lead.mark_contacted()

        elif status == "Qualified":
            lead.qualify()

        elif status == "New":
            lead.status = "New"

        else:
            raise ValueError("Invalid lead status.")

    def delete_lead(self, lead):
        if lead in self.leads:
            self.leads.remove(lead)

    def convert_lead(self, lead):
        client = lead.convert_to_client()

        self.clients.append(client)

        if lead in self.leads:
            self.leads.remove(lead)

        return client

    # -------------------------
    # Project Management
    # -------------------------

    def add_project(self, name, budget, client):
        project = Project(
            name,
            budget,
            client
        )

        client.add_project(project)

        return project

    # -------------------------
    # Invoice Management
    # -------------------------

    def add_invoice(self, project, invoice_id, amount):
        invoice = Invoice(
            invoice_id,
            amount
        )

        project.add_invoice(invoice)

        return invoice