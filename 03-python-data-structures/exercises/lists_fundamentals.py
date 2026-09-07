# Lead Inspector

leads = [
    "ABC Dental",
    "Smile Care Clinic",
    "Bright Health Center",
    "Elite Dermatology",
    "Perfect Smile Dental"
]

print(f"Total Leads: {len(leads)}")
print()
print(f"First Lead: {leads[0]}")
print(f"Last Lead: {leads[-1]}")
print()
print(f"First 3 Leads: {leads[:3]}")
print(f"Last 2 Leads: {leads[-2:]}")
print()
print("ABC Dental" in leads)
print("Google" in leads)