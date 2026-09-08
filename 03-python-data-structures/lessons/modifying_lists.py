# Lists Are Mutable

# append()
# list.append(item)
leads = ["ABC Dental"]
leads.append("XYZ Clinic")
print(leads) # ['ABC Dental', 'XYZ Clinic']

# extend()
leads = ["ABC Dental"]
new_leads = ["XYZ Clinic", "Smile Care"]
leads.extend(new_leads)
print(leads) # ['ABC Dental', 'XYZ Clinic', 'Smile Care']

# insert()
# list.insert(index, value)
leads = ["ABC Dental", "XYZ Clinic"]
leads.insert(0, "New Client")
print(leads) # ['New Client', 'ABC Dental', 'XYZ Clinic']

# remove()
leads = ['ABC Dental', 'XYZ Clinic', 'Smile Care']
leads.remove("XYZ Clinic")
print(leads) # ['ABC Dental', 'Smile Care']

# pop()
# pop() Without an Index
leads = [
    "ABC Dental",
    "XYZ Clinic",
    "Smile Care"
]
leads.pop()
print(leads) # ['ABC Dental', 'XYZ Clinic']

# pop(index)
leads = [
    "ABC Dental",
    "XYZ Clinic",
    "Smile Care"
]
leads.pop(0)
print(leads) # ['XYZ Clinic', 'Smile Care']

# pop() Returns the Removed Value
leads = [
    "ABC Dental",
    "XYZ Clinic",
    "Smile Care"
]
removed_lead = leads.pop()
print(removed_lead) # Smile Care

# Updating List Values
leads = [
    "ABC Dental",
    "XYZ Clinic",
    "Smile Care"
]
leads[0] = "Updated Client"
print(leads) # ['Updated Client', 'XYZ Clinic', 'Smile Care']

# Sorting Lists

# .sort()
numbers = [5, 2, 8, 1, 3]
numbers.sort()
print(numbers) # [1, 2, 3, 5, 8]

# Descending Order
numbers = [5, 2, 8, 1, 3]
numbers.sort(reverse=True)
print(numbers) # [8, 5, 3, 2, 1]

# sorted()
# It creates and returns a sorted result.
numbers = [5, 2, 8, 1, 3]
sorted_numbers = sorted(numbers)
print(sorted_numbers)