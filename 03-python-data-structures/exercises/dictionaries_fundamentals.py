lead = {
    "name": "ABC Dental",
    "country": "Australia",
    "email": "hello@example.com",
    "status": "new",
    "estimated_value": 500.0
}

print("=" * 30)
print("         LEAD REPORT")
print("=" * 30)

for key,value in lead.items():
    print(f"{key}: {value}")