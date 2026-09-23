leads = [
    {
        "name": "Sarah Connor",
        "country": "United States",
        "email": "sarah@example.com",
        "status": "New",
        "estimated_value": 4500
    },
    {
        "name": "Alexandre Dubois",
        "country": "France",
        "email": "alexandre@example.com",
        "status": "Contacted",
        "estimated_value": 12000.50
    },
    {
        "name": "Amina Bello",
        "country": "Nigeria",
        "email": "amina@example.com",
        "status": "Proposal Sent",
        "estimated_value": 8500
    }
]

import json

with open("leads.json", "w", encoding="utf-8") as file:
    json.dump(leads, file, indent=4)

with open("leads.json", "r", encoding="utf-8") as file:
    loaded_leads = json.load(file)

print(loaded_leads)

print(loaded_leads[0])
print(loaded_leads[0]["name"])

for lead in loaded_leads:
    print(lead["name"])


loaded_leads[0]["status"] = "Contacted"

with open("leads.json", "w", encoding="utf-8") as file:
    json.dump(loaded_leads, file, indent=4)
