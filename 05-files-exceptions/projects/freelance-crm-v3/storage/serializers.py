from models import Lead, Client, Project, Invoice


# =========================
# LEAD SERIALIZERS
# =========================

def lead_to_dict(lead: Lead):
    return {
        "id": lead.lead_id,
        "name": lead.name,
        "email": lead.email,
        "country": lead.country,
        "estimated_value": lead.estimated_value,
        "status": lead.status
    }


def lead_from_dict(data: dict):
    return Lead(
        lead_id=data["id"],
        name=data["name"],
        email=data["email"],
        country=data["country"],
        estimated_value=data["estimated_value"],
        status=data["status"]
    )


# =========================
# CLIENT SERIALIZERS
# =========================

def client_to_dict(client: Client):
    return {
        "id": client.client_id,
        "name": client.name,
        "email": client.email,
        "country": client.country,
        "project_ids": [
            project.project_id
            for project in client.projects
        ]
    }


def client_from_dict(data: dict):
    client = Client(
        client_id=data["id"],
        name=data["name"],
        email=data["email"],
        country=data["country"]
    )

    return client


# =========================
# PROJECT SERIALIZERS
# =========================

def project_to_dict(project: Project):
    return {
        "id": project.project_id,
        "name": project.name,
        "client_id": project.client.client_id,
        "budget": project.budget,
        "status": project.status,
        "invoice_ids": [
            invoice.invoice_id
            for invoice in project.invoices
        ]
    }


def project_from_dict(data: dict, client: Client):
    project = Project(
        project_id=data["id"],
        name=data["name"],
        client=client,
        budget=data["budget"],
        status=data["status"]
    )

    return project


# =========================
# INVOICE SERIALIZERS
# =========================

def invoice_to_dict(invoice: Invoice):
    return {
        "id": invoice.invoice_id,
        "amount": invoice.amount,
        "status": invoice.status,
        "project_id": invoice.project.project_id
    }


def invoice_from_dict(data: dict, project: Project):
    invoice = Invoice(
        invoice_id=data["id"],
        amount=data["amount"],
        status=data["status"],
        project=project
    )

    return invoice


# =========================
# CRM SERIALIZERS
# =========================


def crm_to_dict(leads, clients, projects, invoices):
    return {
        "leads": [
            lead_to_dict(lead)
            for lead in leads
        ],
        "clients": [
            client_to_dict(client)
            for client in clients
        ],
        "projects": [
            project_to_dict(project)
            for project in projects
        ],
        "invoices": [
            invoice_to_dict(invoice)
            for invoice in invoices
        ]
    }

def crm_from_dict(data):
    leads = [
        lead_from_dict(lead_data)
        for lead_data in data["leads"]
    ]

    clients = [
        client_from_dict(client_data)
        for client_data in data["clients"]
    ]

    clients_by_id = {
        client.client_id: client
        for client in clients
    }

    projects = []

    for project_data in data["projects"]:
        client = clients_by_id[project_data["client_id"]]

        project = project_from_dict(
            project_data,
            client
        )

        projects.append(project)

        client.projects.append(project)

    projects_by_id = {
        project.project_id: project
        for project in projects
    }

    invoices = []

    for invoice_data in data["invoices"]:
        project = projects_by_id[
            invoice_data["project_id"]
        ]

        invoice = invoice_from_dict(
            invoice_data,
            project
        )

        invoices.append(invoice)

        project.invoices.append(invoice)

    return leads, clients, projects, invoices