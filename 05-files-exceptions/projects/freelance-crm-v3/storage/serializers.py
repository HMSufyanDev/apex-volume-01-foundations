from models import Lead, Client, Project, Invoice


# ==================================================
# LEAD
# ==================================================

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
    lead = Lead(
        lead_id=data["id"],
        name=data["name"],
        email=data["email"],
        country=data["country"],
        estimated_value=data["estimated_value"]
    )

    # JSON stores the current status.
    # Put that status back into the object.
    lead.status = data["status"]

    return lead


# ==================================================
# CLIENT
# ==================================================

def client_to_dict(client: Client):
    return {
        "id": client.client_id,
        "name": client.name,
        "email": client.email,
        "country": client.country,

        # We only store IDs in JSON.
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


# ==================================================
# PROJECT
# ==================================================

def project_to_dict(project: Project):
    return {
        "id": project.project_id,
        "name": project.name,
        "client_id": project.client.client_id,

        # Project stores _budget internally.
        "budget": project._budget,

        "status": project.status,

        # Store invoice IDs instead of whole Invoice objects.
        "invoice_ids": [
            invoice.invoice_id
            for invoice in project.invoices
        ]
    }


def project_from_dict(data: dict, client: Client):
    project = Project(
        project_id=data["id"],
        name=data["name"],
        budget=data["budget"],
        client=client
    )

    # Restore the saved status.
    project.status = data["status"]

    return project


# ==================================================
# INVOICE
# ==================================================

def invoice_to_dict(invoice: Invoice):
    return {
        "id": invoice.invoice_id,
        "amount": invoice._amount,
        "status": invoice.status,

        # Project relationship is stored as an ID.
        "project_id": invoice.project.project_id
    }


def invoice_from_dict(data: dict, project: Project):
    invoice = Invoice(
        invoice_id=data["id"],
        amount=data["amount"],
        project=project
    )

    # Restore saved status.
    invoice.status = data["status"]

    # Connect invoice to its project.
    invoice.project = project

    return invoice


# ==================================================
# COMPLETE CRM → DICTIONARY
# ==================================================

def crm_to_dict(leads, clients):
    
    # We don't have separate projects/invoices lists
    # in CRMService.
    #
    # So we collect them by going through:
    #
    # clients → projects → invoices

    projects = []

    for client in clients:
        for project in client.projects:
            projects.append(project)

    invoices = []

    for project in projects:
        for invoice in project.invoices:
            invoices.append(invoice)

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


# ==================================================
# COMPLETE DICTIONARY → CRM OBJECTS
# ==================================================

def crm_from_dict(data):

    # ----------------------------------------------
    # STEP 1 — Create Leads
    # ----------------------------------------------

    leads = []

    for lead_data in data["leads"]:

        lead = lead_from_dict(lead_data)

        leads.append(lead)


    # ----------------------------------------------
    # STEP 2 — Create Clients
    # ----------------------------------------------

    clients = []

    for client_data in data["clients"]:

        client = client_from_dict(client_data)

        clients.append(client)


    # ----------------------------------------------
    # STEP 3 — Make client ID lookup
    # ----------------------------------------------

    clients_by_id = {
        client.client_id: client
        for client in clients
    }


    # ----------------------------------------------
    # STEP 4 — Create Projects
    # ----------------------------------------------

    projects_by_id = {}

    for project_data in data["projects"]:

        # Find which Client owns this project.
        client = clients_by_id[
            project_data["client_id"]
        ]

        # Create Project object.
        project = project_from_dict(
            project_data,
            client
        )

        # IMPORTANT:
        # Put project inside Client.projects
        client.projects.append(project)

        # Save project in lookup dictionary.
        projects_by_id[
            project.project_id
        ] = project


    # ----------------------------------------------
    # STEP 5 — Create Invoices
    # ----------------------------------------------

    for invoice_data in data["invoices"]:

        # Find the Project that owns this invoice.
        project = projects_by_id[
            invoice_data["project_id"]
        ]

        # Create Invoice object.
        invoice = invoice_from_dict(
            invoice_data,
            project
        )

        # IMPORTANT:
        # Put invoice inside Project.invoices
        project.invoices.append(invoice)


    # ----------------------------------------------
    # STEP 6 — Return CRM memory
    # ----------------------------------------------

    return leads, clients