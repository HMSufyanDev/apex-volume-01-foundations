# A dictionary stores data in key-value pairs.

lead = {
    "name": "ABC Dental",
    "country": "Australia",
    "email": "hello@example.com",
    "status": "new",
    "estimated_value": 500.0
}

# Empty Dictionary
student = {}

student["name"] = "Sufyan"
student["semester"] = 7
print(student) # {'name': 'Sufyan', 'semester': 7}

# Accessing Dictionary Values
lead = {
    "name": "ABC Dental",
    "country": "Australia"
}
print(lead["name"]) # ABC Dental

# Updating a Value
# Dictionaries are mutable.

lead = {
    "name": "ABC Dental",
    "status": "new"
}
lead["status"] = "contacted"
print(lead) # {'name': 'ABC Dental', 'status': 'contacted'}

# Adding a New Key

lead = {
    "name": "ABC Dental",
    "country": "Australia"
}
lead["phone"] = "+123456789"

# What Happens If a Key Doesn't Exist?
lead = {
    "name": "ABC Dental",
    "country": "Australia"
}
print(lead["phone"]) # KeyError: 'phone'

# .get() Method
lead = {
    "name": "ABC Dental",
    "country": "Australia"
}
print(lead.get("phone")) # None

# .get() With a Default Value
# You can give .get() a fallback value.

lead = {
    "name": "ABC Dental",
    "country": "Australia"
}
phone = lead.get("phone", "Not Available")
print(phone) # Not Available

# .keys()
lead = {
    "name": "ABC Dental",
    "country": "Australia",
    "status": "new"
}
print(lead.keys()) # dict_keys(['name', 'country', 'status'])

# .values()
lead = {
    "name": "ABC Dental",
    "country": "Australia",
    "status": "new"
}
print(lead.values()) # dict_values(['ABC Dental', 'Australia', 'new'])

# .items()
lead = {
    "name": "ABC Dental",
    "country": "Australia",
    "status": "new"
}
print(lead.items())
# Output
# dict_items([
#     ('name', 'ABC Dental'),
#     ('country', 'Australia'),
#     ('status', 'new')
# ])
for key, value in lead.items():
    print(key, value)

# Looping Through Dictionary Keys
for key in lead:
    print(key)

# Looping Through Values
for value in lead.values():
    print(value)

# Looping Through Both
for key, value in lead.items():
    print(f"{key}: {value}")

# Accessing a Dictionary Inside a List
leads = [
    {
        "name": "ABC Dental",
        "country": "Australia"
    },
    {
        "name": "XYZ Clinic",
        "country": "Canada"
    }
]
print(leads[0]["name"]) # ABC Dental
