# Project APEX — Week 3

## Python Data Structures

Week 3 of Project APEX focused on understanding Python's core data structures and learning how to work with real-world structured data.

The goal this week was not just to memorize Python syntax, but to understand **how data should be stored, accessed, modified, searched, filtered, and processed**.

I worked with:

* Lists
* Tuples
* Sets
* Dictionaries
* Nested dictionaries
* Lists of dictionaries
* List comprehensions
* Data filtering
* Data grouping
* Data counting
* Data sorting

At the end of the week, I combined these concepts into a complete command-line project:

**Lead Management CLI**

---

# What I Learned

## Day 1 — Lists Fundamentals

The first day focused on understanding lists and why they are useful.

Before lists, multiple values might be stored separately:

```python
lead_1 = "ABC Dental"
lead_2 = "XYZ Clinic"
lead_3 = "Smile Care"
```

A list allows multiple values to be stored together:

```python
leads = ["ABC Dental", "XYZ Clinic", "Smile Care"]
```

### Topics Covered

* What lists are
* Creating lists
* Empty lists
* Lists containing strings
* Lists containing numbers
* Mixed data types
* Positive indexing
* Negative indexing
* Index errors
* List slicing
* `start : stop`
* `len()`
* Membership with `in`
* Membership with `not in`

### Examples

```python
leads = ["ABC Dental", "XYZ Clinic", "Smile Care"]

print(leads[0])
print(leads[-1])
print(leads[:2])
```

I learned that list indexes start from `0` and that the stop position in slicing is not included.

---

# Day 2 — Modifying Lists

The second day focused on changing the contents of lists.

### Topics Covered

* `append()`
* `extend()`
* `insert()`
* `remove()`
* `pop()`
* Updating list values
* `sort()`
* `sorted()`
* Ascending and descending sorting
* Difference between `.sort()` and `sorted()`

### Important Concepts

`append()` adds one item:

```python
leads.append("XYZ Clinic")
```

`extend()` adds multiple items:

```python
leads.extend(["Smile Care", "ABC Dental"])
```

`insert()` adds an item at a specific position:

```python
leads.insert(0, "Priority Client")
```

`remove()` removes an item by value:

```python
leads.remove("ABC Dental")
```

`pop()` removes an item by index and returns the removed value:

```python
removed_lead = leads.pop()
```

I also learned that:

```python
numbers.sort()
```

changes the original list, while:

```python
sorted(numbers)
```

returns a sorted result without modifying the original list.

### Practice

I practiced:

* Managing client lists
* Sorting project prices
* Removing duplicate leads

Duplicate removal was later revisited using Sets.

---

# Day 3 — Tuples + Sets

Day 3 introduced two additional Python data structures: tuples and sets.

---

## Tuples

A tuple is similar to a list but is immutable.

Example:

```python
countries = ("Australia", "Canada", "UK")
```

### Topics Covered

* Creating tuples
* Tuple immutability
* Tuple indexing
* Packing
* Unpacking
* Extended unpacking

Example:

```python
user = "Sufyan", 21, "Pakistan"

name, age, country = user
```

I learned that tuple values cannot be changed after the tuple is created.

I also practiced:

```python
name, *details = user
```

---

## Sets

Sets are useful when unique values are required.

Example:

```python
countries = {"Australia", "Canada", "UK"}
```

Duplicate values are automatically removed.

### Topics Covered

* Creating sets
* Unique values
* Removing duplicates
* Union
* Intersection
* Difference

Examples:

```python
agency_a | agency_b
```

```python
agency_a & agency_b
```

```python
agency_a - agency_b
```

I practiced using Sets to:

* Remove duplicate leads
* Find common agency services
* Find services unique to each agency

---

# Day 4 — Dictionaries Fundamentals

Day 4 focused on dictionaries.

This was one of the most important topics of the week because the final project uses dictionaries heavily.

Dictionaries store data as:

```text
key → value
```

Example:

```python
lead = {
    "name": "ABC Dental",
    "country": "Australia",
    "email": "hello@example.com",
    "status": "new",
    "estimated_value": 500.0
}
```

### Topics Covered

* Dictionary structure
* Key-value pairs
* Accessing values
* Updating values
* Adding new keys
* `.get()`
* `.keys()`
* `.values()`
* `.items()`
* Looping through dictionary items

Examples:

```python
print(lead["name"])
```

Updating:

```python
lead["status"] = "contacted"
```

Adding:

```python
lead["phone"] = "+123456789"
```

Safer access:

```python
lead.get("phone", "Not Available")
```

Looping:

```python
for key, value in lead.items():
    print(key, value)
```

I learned that dictionaries are useful for representing real-world objects because each object can contain multiple related properties.

---

# Day 5 — Advanced Dictionaries + Data Processing

Day 5 combined the data structures from the previous days.

This was the point where the concepts started becoming more practical.

---

## Nested Dictionaries

I learned how one dictionary can contain another dictionary.

Example:

```python
lead = {
    "name": "ABC Dental",
    "country": "Australia",
    "contact": {
        "email": "hello@example.com",
        "phone": "123456"
    }
}
```

Accessing nested data:

```python
lead["contact"]["email"]
```

---

## Lists of Dictionaries

This became one of the most important structures of the week.

```python
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
```

This structure allows an application to store multiple real-world objects.

Each dictionary represents one lead, while the list stores all leads.

---

## List Comprehensions

I learned how to create lists in a shorter and more readable way.

Normal approach:

```python
squares = []

for number in numbers:
    squares.append(number ** 2)
```

List comprehension:

```python
squares = [number ** 2 for number in numbers]
```

I also learned filtering with comprehensions:

```python
even_numbers = [
    number
    for number in numbers
    if number % 2 == 0
]
```

And real-world filtering:

```python
new_leads = [
    lead
    for lead in leads
    if lead["status"] == "new"
]
```

---

## Sorting Structured Data

I learned how to sort dictionaries based on one of their values.

Example:

```python
sorted_clients = sorted(
    clients,
    key=lambda client: client["price"]
)
```

I also learned how to reverse the order:

```python
sorted_clients = sorted(
    clients,
    key=lambda client: client["price"],
    reverse=True
)
```

---

## Grouping Data

I practiced grouping leads by country.

The general idea was:

```text
Lead
 ↓
Read country
 ↓
Find/create country group
 ↓
Add lead to that group
```

Using:

```python
grouped_leads.setdefault(country, []).append(lead)
```

This produces a structure such as:

```python
{
    "Australia": [...],
    "Canada": [...],
    "UK": [...]
}
```

---

## Counting Data

I also practiced counting leads by status.

Example result:

```python
{
    "new": 5,
    "contacted": 3,
    "converted": 2
}
```

The general counting pattern was:

```python
if value not in counts:
    counts[value] = 0

counts[value] += 1
```

---

## Filtering Data

I practiced filtering structured data, such as unpaid invoices:

```python
unpaid = [
    invoice
    for invoice in invoices
    if not invoice["paid"]
]
```

---

## Word Frequency

I also built a simple word-frequency counter.

Given:

```python
text = "python data python lists data python"
```

The result was:

```python
{
    "python": 3,
    "data": 2,
    "lists": 1
}
```

This helped reinforce dictionaries, loops, strings, and counting logic.

---

# Day 6 — Weekly Project

## Lead Management CLI

The final day was used to combine everything learned throughout the week into a practical command-line application.

The application stores leads using:

```python
leads = []
```

Each lead is represented as a dictionary:

```python
{
    "name": "ABC Dental",
    "country": "Australia",
    "email": "hello@example.com",
    "status": "new",
    "estimated_value": 500.0
}
```

So the complete structure is:

```text
List
 ├── Dictionary (Lead 1)
 ├── Dictionary (Lead 2)
 ├── Dictionary (Lead 3)
 └── Dictionary (Lead 4)
```

### Features Built

The application includes:

1. Add Lead
2. View All Leads
3. Search Leads
4. Update Lead Status
5. Delete Lead
6. Calculate Pipeline Value
7. Filter by Country
8. Filter by Status
9. Exit

---

# Skills Used in the Project

The final project brought together almost everything learned during Week 3:

* Lists
* Dictionaries
* List indexing
* List modification
* `append()`
* `remove()`
* Loops
* Conditions
* Dictionary access
* Dictionary updates
* List comprehensions
* String methods
* Searching
* Filtering
* `sum()`
* `enumerate()`
* Structured data processing

---

# Key Lessons From Week 3

The biggest lesson from this week was learning that data structures are not isolated concepts.

They work together.

For example:

```python
leads = [
    {
        "name": "ABC Dental",
        "country": "Australia",
        "status": "new",
        "estimated_value": 500
    }
]
```

contains:

```text
List
 ↓
Dictionary
 ↓
Key → Value
```

And when processing it:

```python
for lead in leads:
    if lead["status"] == "new":
        print(lead["name"])
```

I am combining:

```text
List
+
Dictionary
+
Loop
+
Condition
+
Dictionary Access
```

This is much closer to how real applications process data.

---


# Week 3 Outcome

By completing Week 3, I can now:

* Store multiple values using Lists
* Access and modify list elements
* Add and remove list data
* Sort lists
* Understand immutable Tuples
* Pack and unpack Tuples
* Remove duplicates using Sets
* Perform Set operations
* Store structured information using Dictionaries
* Access and update dictionary values
* Work with nested Dictionaries
* Work with Lists of Dictionaries
* Filter data
* Sort structured data
* Group data
* Count data
* Use List Comprehensions
* Build a real CLI application around structured data

The main progression was:

```text
Lists
   ↓
Tuples + Sets
   ↓
Dictionaries
   ↓
Lists of Dictionaries
   ↓
Data Processing
   ↓
Lead Management CLI
```

---

# Project APEX Progress

**Week 3 — Completed ✅**

### Previous

* Week 1 — Python Foundations ✅
* Week 2 — Functions and Modular Thinking ✅

### Current

* Week 3 — Python Data Structures ✅

### Main Project

**Lead Management CLI**

Week 3 strengthened my understanding of how Python stores and processes structured data and prepared me for more advanced backend and software engineering concepts in the upcoming weeks.
