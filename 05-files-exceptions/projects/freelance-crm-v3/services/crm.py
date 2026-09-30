from models import Project, Invoice
from storage.serializers import (
    crm_from_dict,
    crm_to_dict
)

class CRMService:

    def __init__(self, storage):
        self.storage = storage
        self.leads = []
        self.clients = []



    # -------------------------
    # Storage Management
    # -------------------------
    
    def load(self):

        data = self.storage.storage_load()

        self.leads, self.clients = crm_from_dict(data)


    def save(self):

        data = crm_to_dict(
            self.leads,
            self.clients
        )

        self.storage.storage_save(data)



    # -------------------------
    # Lead Management
    # -------------------------

    def add_lead(self, lead):
        self.leads.append(lead)
        self.save()

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

        self.save()

    def delete_lead(self, lead):
        if lead in self.leads:
            self.leads.remove(lead)
            self.save()

    def convert_lead(self, lead, client_id):
        client = lead.convert_to_client(client_id)

        self.clients.append(client)

        if lead in self.leads:
            self.leads.remove(lead)

        self.save()

        return client

    # -------------------------
    # Project Management
    # -------------------------

    def add_project(self, project_id, name, budget, client):
        project = Project(
            project_id,
            name,
            budget,
            client
        )

        client.add_project(project)

        self.save()

        return project

    def update_project_status(self, project, status):

        project.update_status(status)

        self.save()

    # -------------------------
    # Invoice Management
    # -------------------------

    def add_invoice(self, project, invoice_id, amount):
        invoice = Invoice(
            invoice_id,
            amount,
            project
        )

        project.add_invoice(invoice)

        self.save()

        return invoice

    def mark_invoice_paid(self, invoice):

        invoice.mark_paid()

        self.save()