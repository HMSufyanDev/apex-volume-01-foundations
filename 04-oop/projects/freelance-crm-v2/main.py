
from models.lead import Lead
from services.crm import CRMService


# ========================================
# Helper Functions
# ========================================

def print_header():
    print("\n" + "=" * 40)
    print("       FREELANCE CRM V2")
    print("=" * 40)


def pause():
    input("\nPress Enter to continue...")


def get_positive_float(prompt):
    while True:
        try:
            value = float(input(prompt))

            if value < 0:
                print("Value cannot be negative.")
                continue

            return value

        except ValueError:
            print("Please enter a valid number.")


def get_lead_by_index(crm):
    if not crm.leads:
        print("\nNo leads available.")
        return None

    print("\n--- Leads ---")

    for index, lead in enumerate(crm.leads, start=1):
        print(
            f"{index}. {lead.name} | "
            f"{lead.email} | "
            f"{lead.status} | "
            f"${lead.estimated_value:,.2f}"
        )

    while True:
        try:
            choice = int(input("\nEnter lead number: "))

            if 1 <= choice <= len(crm.leads):
                return crm.leads[choice - 1]

            print("Invalid lead number.")

        except ValueError:
            print("Please enter a valid number.")


def get_client_by_index(crm):
    if not crm.clients:
        print("\nNo clients available.")
        return None

    print("\n--- Clients ---")

    for index, client in enumerate(crm.clients, start=1):
        print(
            f"{index}. {client.name} | "
            f"{client.email} | "
            f"{client.country} | "
            f"Projects: {len(client.projects)}"
        )

    while True:
        try:
            choice = int(input("\nEnter client number: "))

            if 1 <= choice <= len(crm.clients):
                return crm.clients[choice - 1]

            print("Invalid client number.")

        except ValueError:
            print("Please enter a valid number.")


def get_project_by_index(client):
    if not client.projects:
        print("\nThis client has no projects.")
        return None

    print(f"\n--- Projects for {client.name} ---")

    for index, project in enumerate(client.projects, start=1):
        print(
            f"{index}. {project.name} | "
            f"Budget: ${project.budget:,.2f} | "
            f"Status: {project.status}"
        )

    while True:
        try:
            choice = int(input("\nEnter project number: "))

            if 1 <= choice <= len(client.projects):
                return client.projects[choice - 1]

            print("Invalid project number.")

        except ValueError:
            print("Please enter a valid number.")


def get_invoice_by_index(project):
    if not project.invoices:
        print("\nThis project has no invoices.")
        return None

    print(f"\n--- Invoices for {project.name} ---")

    for index, invoice in enumerate(project.invoices, start=1):
        print(
            f"{index}. "
            f"{invoice.invoice_id} | "
            f"${invoice.amount:,.2f} | "
            f"{invoice.status}"
        )

    while True:
        try:
            choice = int(input("\nEnter invoice number: "))

            if 1 <= choice <= len(project.invoices):
                return project.invoices[choice - 1]

            print("Invalid invoice number.")

        except ValueError:
            print("Please enter a valid number.")


# ========================================
# Lead Management
# ========================================

def add_lead(crm):
    print("\n--- Add Lead ---")

    name = input("Name: ").strip()
    email = input("Email: ").strip()
    country = input("Country: ").strip()
    estimated_value = get_positive_float("Estimated value ($): ")

    lead = Lead(
        name,
        email,
        country,
        estimated_value
    )

    crm.add_lead(lead)

    print("\nLead added successfully.")


def view_leads(crm):
    print("\n--- All Leads ---")

    if not crm.leads:
        print("No leads available.")
        return

    for index, lead in enumerate(crm.leads, start=1):
        print(
            f"\n{index}. "
            f"Name: {lead.name}"
        )
        print(f"   Email: {lead.email}")
        print(f"   Country: {lead.country}")
        print(f"   Status: {lead.status}")
        print(f"   Estimated Value: ${lead.estimated_value:,.2f}")


def search_lead(crm):
    print("\n--- Search Lead ---")

    query = input(
        "Enter name or email to search: "
    ).strip()

    results = crm.search_lead(query)

    if not results:
        print("\nNo leads found.")
        return

    print(f"\nFound {len(results)} lead(s):")

    for index, lead in enumerate(results, start=1):
        print(
            f"\n{index}. {lead.name}"
        )
        print(f"   Email: {lead.email}")
        print(f"   Country: {lead.country}")
        print(f"   Status: {lead.status}")
        print(f"   Estimated Value: ${lead.estimated_value:,.2f}")


def update_lead(crm):
    print("\n--- Update Lead ---")

    lead = get_lead_by_index(crm)

    if lead is None:
        return

    print(f"\nSelected Lead: {lead.name}")
    print(f"Current Status: {lead.status}")

    print("\nAvailable statuses:")
    print("1. New")
    print("2. Contacted")
    print("3. Qualified")

    choice = input("\nChoose new status: ").strip()

    status_map = {
        "1": "New",
        "2": "Contacted",
        "3": "Qualified"
    }

    if choice not in status_map:
        print("Invalid choice.")
        return

    try:
        crm.update_lead_status(
            lead,
            status_map[choice]
        )

        print("\nLead status updated successfully.")

    except ValueError as error:
        print(error)


def delete_lead(crm):
    print("\n--- Delete Lead ---")

    lead = get_lead_by_index(crm)

    if lead is None:
        return

    print(f"\nSelected: {lead.name}")

    confirmation = input(
        "Are you sure you want to delete this lead? (y/n): "
    ).strip().lower()

    if confirmation == "y":
        crm.delete_lead(lead)
        print("\nLead deleted successfully.")

    else:
        print("\nDelete cancelled.")


# ========================================
# Lead Conversion
# ========================================

def convert_lead(crm):
    print("\n--- Convert Lead ---")

    lead = get_lead_by_index(crm)

    if lead is None:
        return

    print(f"\nSelected Lead: {lead.name}")
    print(f"Current Status: {lead.status}")

    confirmation = input(
        "Convert this lead to a client? (y/n): "
    ).strip().lower()

    if confirmation != "y":
        print("\nConversion cancelled.")
        return

    try:
        client = crm.convert_lead(lead)

        print("\nLead converted successfully!")
        print(f"Client: {client.name}")
        print(f"Email: {client.email}")
        print(f"Country: {client.country}")

    except ValueError as error:
        print(f"\nError: {error}")


# ========================================
# Client Management
# ========================================

def view_clients(crm):
    print("\n--- All Clients ---")

    if not crm.clients:
        print("No clients available.")
        return

    for index, client in enumerate(crm.clients, start=1):

        print(
            f"\n{index}. {client.name}"
        )
        print(f"   Email: {client.email}")
        print(f"   Country: {client.country}")
        print(f"   Projects: {len(client.projects)}")
        print(
            f"   Total Revenue: "
            f"${client.get_total_revenue():,.2f}"
        )
        print(
            f"   Paid Revenue: "
            f"${client.get_paid_revenue():,.2f}"
        )
        print(
            f"   Outstanding: "
            f"${client.get_outstanding_revenue():,.2f}"
        )


# ========================================
# Project Management
# ========================================

def add_project(crm):
    print("\n--- Add Project ---")

    client = get_client_by_index(crm)

    if client is None:
        return

    print(f"\nSelected Client: {client.name}")

    name = input("Project name: ").strip()
    budget = get_positive_float("Project budget ($): ")

    project = crm.add_project(
        name,
        budget,
        client
    )

    print("\nProject added successfully.")
    print(f"Project: {project.name}")
    print(f"Budget: ${project.budget:,.2f}")
    print(f"Status: {project.status}")


def update_project_status(crm):
    print("\n--- Update Project Status ---")

    client = get_client_by_index(crm)

    if client is None:
        return

    project = get_project_by_index(client)

    if project is None:
        return

    print(f"\nSelected Project: {project.name}")
    print(f"Current Status: {project.status}")

    print("\nAvailable statuses:")

    statuses = [
        "Planning",
        "In Progress",
        "Completed",
        "Cancelled"
    ]

    for index, status in enumerate(statuses, start=1):
        print(f"{index}. {status}")

    choice = input("\nChoose new status: ").strip()

    try:
        status = statuses[int(choice) - 1]

    except (ValueError, IndexError):
        print("Invalid choice.")
        return

    try:
        project.update_status(status)

        print("\nProject status updated successfully.")

    except ValueError as error:
        print(error)


# ========================================
# Invoice Management
# ========================================

def create_invoice(crm):
    print("\n--- Create Invoice ---")

    client = get_client_by_index(crm)

    if client is None:
        return

    project = get_project_by_index(client)

    if project is None:
        return

    invoice_id = input(
        "Invoice ID: "
    ).strip()

    amount = get_positive_float(
        "Invoice amount ($): "
    )

    invoice = crm.add_invoice(
        project,
        invoice_id,
        amount
    )

    print("\nInvoice created successfully.")
    print(invoice)


def mark_invoice_paid(crm):
    print("\n--- Mark Invoice Paid ---")

    client = get_client_by_index(crm)

    if client is None:
        return

    project = get_project_by_index(client)

    if project is None:
        return

    invoice = get_invoice_by_index(project)

    if invoice is None:
        return

    if invoice.status == "Paid":
        print("\nThis invoice is already paid.")
        return

    invoice.mark_paid()

    print("\nInvoice marked as paid.")
    print(invoice)


# ========================================
# Client History
# ========================================

def client_history(crm):
    print("\n--- Client History ---")

    client = get_client_by_index(crm)

    if client is None:
        return

    history = client.get_history()

    print(f"\nClient: {history['client']}")

    if not history["projects"]:
        print("\nNo projects found.")
        return

    for project in history["projects"]:

        print("\n" + "-" * 40)

        print(f"Project: {project['name']}")
        print(f"Status: {project['status']}")
        print(
            f"Revenue: "
            f"${project['revenue']:,.2f}"
        )

        print("\nInvoices:")

        if not project["invoices"]:
            print("  No invoices.")

        else:
            for invoice in project["invoices"]:
                print(
                    f"  - {invoice.invoice_id} | "
                    f"${invoice.amount:,.2f} | "
                    f"{invoice.status}"
                )


# ========================================
# Main Menu
# ========================================

def show_menu():

    print_header()

    print("\n1.  Add Lead")
    print("2.  View Leads")
    print("3.  Search Lead")
    print("4.  Update Lead")
    print("5.  Delete Lead")
    print("6.  Convert Lead")
    print("7.  View Clients")
    print("8.  Add Project")
    print("9.  Update Project Status")
    print("10. Create Invoice")
    print("11. Mark Invoice Paid")
    print("12. Client History")
    print("13. Exit")


def main():

    crm = CRMService()

    while True:

        show_menu()

        choice = input("\nChoose an option: ").strip()

        if choice == "1":
            add_lead(crm)

        elif choice == "2":
            view_leads(crm)

        elif choice == "3":
            search_lead(crm)

        elif choice == "4":
            update_lead(crm)

        elif choice == "5":
            delete_lead(crm)

        elif choice == "6":
            convert_lead(crm)

        elif choice == "7":
            view_clients(crm)

        elif choice == "8":
            add_project(crm)

        elif choice == "9":
            update_project_status(crm)

        elif choice == "10":
            create_invoice(crm)

        elif choice == "11":
            mark_invoice_paid(crm)

        elif choice == "12":
            client_history(crm)

        elif choice == "13":
            print("\nThank you for using Freelance CRM V2.")
            print("Goodbye!")
            break

        else:
            print("\nInvalid option. Please choose 1-13.")

        pause()


# ========================================
# Program Entry Point
# ========================================

if __name__ == "__main__":
    main()

