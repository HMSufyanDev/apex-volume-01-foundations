leads = []

def add_lead():
    name = input("Enter lead name: ")
    country = input("Enter country: ")
    email = input("Enter email: ")
    status = input("Enter status: ")
    estimated_value = float(input("Enter estimated value: "))

    lead = {
    "name": name,
    "country": country,
    "email": email,
    "status": status,
    "estimated_value": estimated_value
    }

    leads.append(lead)

def view_all_leads():
    for index, lead in enumerate(leads, start=1):
        print("=" * 30)
        print(f"Lead # {index}")
        print("=" * 30)
        print()
        print(f"Name: {lead["name"]}")
        print(f"Country: {lead["country"]}")
        print(f"Email: {lead["email"]}")
        print(f"Status: {lead["status"]}")
        print(f"Estimated Value: {lead["estimated_value"]}")
        print()

def search_leads():
    query = input("Search lead: ").lower()
    for lead in leads:
        if query in lead["name"].lower() or query in lead["country"].lower():
            print(lead)


def update_lead_status():
    while True:
        search_name = input("Enter lead name: ").strip().lower()

        for lead in leads:
            if lead["name"].lower() == search_name:
                new_status = input("Enter new status: ").strip()
                lead["status"] = new_status
                print("Lead status updated successfully.")
                return  

        print("Lead not found. Please try again.\n")
    




