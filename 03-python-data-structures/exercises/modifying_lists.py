# Remove Duplicate Leads

leads = [
    "ABC Dental",
    "XYZ Clinic",
    "ABC Dental",
    "Smile Care",
    "XYZ Clinic"
]

updated_leads = []

for lead in leads:
    if  lead not in updated_leads:
        updated_leads.append(lead)

print(updated_leads) # ['ABC Dental', 'XYZ Clinic', 'Smile Care']



# Mini Lead Manager
leads = [
    "ABC Dental",
    "XYZ Clinic",
    "Smile Care"
]

print("=" * 30)
print("LEAD MANAGEMENT REPORT")
print("=" * 30)

print()
print(f"Current Leads: {leads}")

leads.append("Bright Health")
print(f"After append: {leads}")

leads.insert(0, "Priority Dental")
print(f"After priority insert: {leads}")

leads[2] = "Updated lead"
print(f"After update existing lead: {leads}")

leads.remove("Smile Care")
print(f"After remove lead: {leads}")

removed_lead = leads.pop()
print(f"Removed lead: {removed_lead}")
print(f"After remove lead: {leads}")

leads.sort()
print(f"Sorted list: {leads}")

