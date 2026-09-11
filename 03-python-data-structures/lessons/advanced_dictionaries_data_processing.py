# Nested Dictionaries
lead = {
    "name": "ABC Dental",
    "country": "Australia",
    "contact": {
        "email": "hello@example.com",
        "phone": "123456"
    }
}

# Accessing Nested Values
lead["contact"]["email"] # hello@example.com

# Updating Nested Values
lead["contact"]["phone"] = "999999"

# Lists of Dictionaries
leads = [
    {
        "name": "ABC Dental",
        "country": "Australia",
        "status": "new",
        "estimated_value": 500.0
    },
    {
        "name": "XYZ Clinic",
        "country": "Canada",
        "status": "contacted",
        "estimated_value": 800.0
    }
]

# Accessing a Property of a Lead
print(leads[0]["name"]) # ABC Dental

# Looping Through a List of Dictionaries
for lead in leads:
    print(lead["name"]) # ABC Dental # XYZ Clinic

# Filtering Leads With a Loop
for lead in leads:
    if lead["status"] == "new":
        print(lead["name"])

# List Comprehensions
numbers = [1, 2, 3, 4, 5]
squares = [number ** 2 for number in numbers]

# List Comprehension With Filtering
even_numbers = [
    number
    for number in numbers
    if number % 2 == 0
] # [2, 4, 6]

# Extracting Specific Values
lead_names = [
    lead["name"]
    for lead in leads
]

# Sorting Dictionaries
clients = [
    {"name": "Client A", "price": 500},
    {"name": "Client B", "price": 1200},
    {"name": "Client C", "price": 800}
]

# sorted() With key=
sorted_clients = sorted(
    clients,
    key = lambda client: client["price"]
)

# Descending Order
sorted_clients = sorted(
    clients,
    key=lambda client: client["price"],
    reverse=True
)

# setdefault()
person = {"name": "Alice"}

# 1. Key DOES NOT exist ("age")
# Python adds "age": 18 to the dictionary and returns 18
age = person.setdefault("age", 18)

print(age)     # 18
print(person)  # {'name': 'Alice', 'age': 18}


# 2. Key ALREADY exists ("name")
# Python keeps "Alice" (ignores "Bob") and returns "Alice"
name = person.setdefault("name", "Bob")

print(name)    # Alice
print(person)  # {'name': 'Alice', 'age': 18}

# Group Leads by Country
leads = [
    {"name": "ABC Dental", "country": "Australia"},
    {"name": "XYZ Clinic", "country": "Canada"},
    {"name": "Smile Care", "country": "Australia"},
    {"name": "Bright Dental", "country": "UK"}
]

# Start With an Empty Dictionary
grouped_leads = {}
for lead in leads:
    country = lead["country"]
    grouped_leads.setdefault(country, []).append(lead)

print(grouped_leads)

# Count Leads by Status
leads = [
    {"name": "A", "status": "new"},
    {"name": "B", "status": "contacted"},
    {"name": "C", "status": "new"},
    {"name": "D", "status": "converted"},
    {"name": "E", "status": "new"}
]

status_counts = {}
for lead in leads:
    status = lead["status"]
    if status not in status_counts:
        status_counts[status] = 0
    status_counts[status] += 1
print(status_counts)

# Filter Unpaid Invoices
invoices = [
    {"client": "A", "paid": True},
    {"client": "B", "paid": False},
    {"client": "C", "paid": False}
]

unpaid = [invoice for invoice in invoices if not invoice["paid"]]
print(unpaid)