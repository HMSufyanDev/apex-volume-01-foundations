leads = [
    {
        "name": "Sarah Connor",
        "country": "United States",
        "email": "sarah.connor@cyberdyne.io",
        "status": "New",
        "estimated_value": 4500.0
    },
    {
        "name": "Alexandre Dubois",
        "country": "France",
        "email": "a.dubois@techsolutions.fr",
        "status": "In Contact",
        "estimated_value": 12000.50
    },
    {
        "name": "Amina Bello",
        "country": "Nigeria",
        "email": "amina@globalinnovations.ng",
        "status": "Proposal Sent",
        "estimated_value": 8500.00
    },
    {
        "name": "Kenji Sato",
        "country": "Japan",
        "email": "kenji.sato@sato-logistics.jp",
        "status": "Qualified",
        "estimated_value": 15000.75
    },
    {
        "name": "Elena Rostova",
        "country": "Germany",
        "email": "e.rostova@berlin-ventures.de",
        "status": "Closed Won",
        "estimated_value": 22000.00
    }
]

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
        print()
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
    while True:
        query = input("Search lead: ").lower()
            
        for lead in leads:
            if query in lead["name"].lower() or query in lead["country"].lower():
                print()
                print("=" * 20)
                print(f"Lead Info")
                print("=" * 20)
                print()
                print(f"Name: {lead["name"]}")
                print(f"Country: {lead["country"]}")
                print(f"Email: {lead["email"]}")
                print(f"Status: {lead["status"]}")
                print(f"Estimated Value: {lead["estimated_value"]}")
                print()
                return

        print("Lead not found. Please try again.\n")
            


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
    

def delete_lead():
    while True:
        search_name = input("Enter lead name: ").strip().lower()
        for lead in leads:
            if lead["name"].lower() == search_name:
                leads.remove(lead)
                print("Lead delete successfully.")
                return
        print("Lead not found. Please try again.\n")


def calculate_pipeline_value():
    total = sum(
    lead["estimated_value"]
    for lead in leads
    )

    print()
    print(f"Total Pipeline Value: ${total:,.2f}")


def filter_by_country():
    search_country = input("Enter leads country: ").strip().lower()

    filter_lead = [lead for lead in leads if lead["country"].lower() == search_country]
  
    for index, lead in enumerate(filter_lead, start=1):
        print()
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

    if not filter_lead:
        print("No lead found!")


def filter_by_status():
    search_status = input("Enter leads status: ").strip().lower()

    filter_lead = [lead for lead in leads if lead["status"].lower() == search_status]

    for index, lead in enumerate(filter_lead, start=1):
        print()
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

    if not filter_lead:
            print("No lead found!")
