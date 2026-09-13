# Lead Management CLI

A command-line Python application for managing freelance leads and potential clients.

This project was built as the **weekly project for Project APEX — Week 3: Python Data Structures**.

The main goal of this project was to take the Python data structures and data-processing concepts learned throughout Week 3 and combine them into a practical application.

---

# Project Overview

When doing freelance outreach, you may have many potential clients.

For example:

```text
Sarah Connor
Alexandre Dubois
Amina Bello
Kenji Sato
Elena Rostova
```

Instead of storing only their names, a useful lead record needs more information.

Each lead in this project contains:

```text
Name
Country
Email
Status
Estimated Project Value
```

The application stores each lead as a **dictionary**, while all leads are stored inside a **list**.

The basic structure is:

```python
leads = [
    {
        "name": "Sarah Connor",
        "country": "United States",
        "email": "sarah.connor@cyberdyne.io",
        "status": "New",
        "estimated_value": 4500.0
    }
]
```

This makes the project a practical example of a:

**List of Dictionaries**

---

# Features

The application currently provides **8 lead-management operations**.

## 1. Add Lead

Allows the user to create and add a new lead.

The application asks for:

* Lead name
* Country
* Email
* Status
* Estimated value

Example:

```text
Enter lead name: John Smith
Enter country: Australia
Enter email: john@example.com
Enter status: New
Enter estimated value: 5000
```

The new lead is stored as a dictionary and added to the `leads` list using `append()`.

```python
leads.append(lead)
```

---

## 2. View All Leads

Displays every lead currently stored in the list.

The program uses `enumerate()` to display each lead with a 1-based lead number.

Example:

```text
==============================
Lead # 1
==============================

Name: Sarah Connor
Country: United States
Email: sarah.connor@cyberdyne.io
Status: New
Estimated Value: 4500.0
```

The leads are displayed by looping through the `leads` list.

---

## 3. Search Leads

Allows the user to search for a lead by:

* Name
* Country

The search is **case-insensitive** because `.lower()` is used.

For example:

```text
Search lead: japan
```

can find:

```text
Kenji Sato
```

The search works by checking whether the entered query exists inside the lead's name or country.

```python
if query in lead["name"].lower() or query in lead["country"].lower():
```

If a matching lead is found, its information is displayed.

If no lead is found, the application allows the user to try again or return to the main menu.

---

## 4. Update Lead Status

Allows the user to update the status of an existing lead.

The program searches for the lead using its **exact name**, ignoring capitalization.

For example:

```text
Enter lead name: Sarah Connor
Enter new status: In Contact
```

The status is then updated directly inside the dictionary:

```python
lead["status"] = new_status
```

The project does **not** restrict the user to a fixed list of statuses. The user can enter any status they want.

Examples could include:

```text
New
In Contact
Qualified
Proposal Sent
Closed Won
Closed Lost
```

---

## 5. Delete Lead

Allows the user to remove a lead from the `leads` list.

The program searches for a lead by its exact name, ignoring capitalization.

When the lead is found, it is removed using:

```python
leads.remove(lead)
```

If the lead cannot be found, the program allows the user to try again or return to the menu.

---

## 6. Calculate Pipeline Value

Calculates the total estimated value of all leads currently stored in the system.

The calculation uses Python's `sum()` function together with a generator expression:

```python
total = sum(
    lead["estimated_value"]
    for lead in leads
)
```

The result is displayed as a formatted currency value:

```text
Total Pipeline Value: $62,023.25
```

The pipeline value represents the combined estimated value of all current leads.

---

## 7. Filter by Country

Displays only the leads belonging to a specific country.

The country search is case-insensitive.

For example:

```text
Enter leads country: Germany
```

The program creates a new filtered list using a **list comprehension**:

```python
filter_lead = [
    lead
    for lead in leads
    if lead["country"].lower() == search_country
]
```

If matching leads exist, they are displayed.

If there are no matches:

```text
No lead found!
```

---

## 8. Filter by Status

Displays only leads with a specific status.

The status search is case-insensitive.

For example:

```text
Enter leads status: Qualified
```

The application uses a list comprehension to create a filtered list:

```python
filter_lead = [
    lead
    for lead in leads
    if lead["status"].lower() == search_status
]
```

Matching leads are then displayed.

If no matching leads exist:

```text
No lead found!
```

---

# Application Menu

The main application provides the following menu:

```text
==================================================
              LEAD MANAGEMENT SYSTEM
==================================================
1. Add Lead
2. View All Leads
3. Search Leads
4. Update Lead Status
5. Delete Lead
6. Calculate Pipeline Value
7. Filter by Country
8. Filter by Status
9. Exit
```

The user selects an option from `1` to `9`.

The program continues running inside a `while True` loop until the user selects option `9`.

---

# Initial Mock Data

The project currently starts with five mock leads for testing.

```text
Sarah Connor
United States
New
$4,500.00
```

```text
Alexandre Dubois
France
In Contact
$12,000.50
```

```text
Amina Bello
Nigeria
Proposal Sent
$8,500.00
```

```text
Kenji Sato
Japan
Qualified
$15,000.75
```

```text
Elena Rostova
Germany
Closed Won
$22,000.00
```

These leads are stored in `leads.py`:

```python
leads = [
    {
        "name": "...",
        "country": "...",
        "email": "...",
        "status": "...",
        "estimated_value": ...
    }
]
```

The mock data makes it possible to test searching, filtering, updating, deleting, and pipeline calculations immediately after starting the program.

---

# Data Structure

The central concept of this project is the combination of **lists and dictionaries**.

## List

All leads are stored inside one list:

```python
leads = []
```

A list allows the application to store multiple lead records.

---

## Dictionary

Each individual lead is represented by a dictionary:

```python
lead = {
    "name": "Sarah Connor",
    "country": "United States",
    "email": "sarah.connor@cyberdyne.io",
    "status": "New",
    "estimated_value": 4500.0
}
```

Each key represents a different piece of information about the lead.

---

## List of Dictionaries

Combining both structures creates:

```python
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
    }
]
```

Conceptually:

```text
leads
│
├── Lead 1
│   └── Dictionary
│
├── Lead 2
│   └── Dictionary
│
├── Lead 3
│   └── Dictionary
│
└── Lead 4
    └── Dictionary
```

This structure is useful because it closely represents how real application data can be organized.

---

# Python Concepts Practiced

This project was built to practice the concepts covered during **Project APEX Week 3**.

## Lists

Used to store all lead records:

```python
leads = []
```

---

## `append()`

Used to add a new lead to the list:

```python
leads.append(lead)
```

---

## `remove()`

Used to delete an existing lead:

```python
leads.remove(lead)
```

---

## Dictionaries

Each lead is represented as a dictionary:

```python
{
    "name": "...",
    "country": "...",
    "email": "...",
    "status": "...",
    "estimated_value": ...
}
```

---

## Dictionary Access

Values are accessed using dictionary keys:

```python
lead["name"]
lead["country"]
lead["email"]
lead["status"]
lead["estimated_value"]
```

---

## Dictionary Updating

The lead status can be changed directly:

```python
lead["status"] = new_status
```

---

## `for` Loops

Loops are used to process leads:

```python
for lead in leads:
    ...
```

For example, the application uses loops when displaying, searching, updating, and deleting leads.

---

## `enumerate()`

Used to display lead numbers starting from `1`:

```python
for index, lead in enumerate(leads, start=1):
    ...
```

---

## List Comprehensions

Used for filtering leads.

For example:

```python
filter_lead = [
    lead
    for lead in leads
    if lead["country"].lower() == search_country
]
```

---

## String Methods

`.lower()` is used to make searches case-insensitive:

```python
lead["name"].lower()
```

`.strip()` is also used when receiving some user input:

```python
input(...).strip()
```

---

## `sum()`

Used to calculate the total pipeline value:

```python
total = sum(
    lead["estimated_value"]
    for lead in leads
)
```

---

## Generator Expression

The pipeline calculation uses a generator expression inside `sum()`:

```python
lead["estimated_value"]
for lead in leads
```

This processes the estimated values of all leads without creating a separate list just for the calculation.

---

## `while` Loops

Some operations use `while True` to allow the user to retry when a lead is not found.

For example:

```python
while True:
    ...
```

The loop ends when a matching lead is found or when the user chooses to return.

---

## `if` Conditions

Conditions are used throughout the application to make decisions.

For example:

```python
if query in lead["name"].lower():
    ...
```

and:

```python
if choice == '1':
    leads.add_lead()
```

---

## Modules and Imports

The project is separated into two Python files.

`main.py` imports the `leads` module:

```python
import leads
```

This allows the main program to call functions from `leads.py`.

---

# Project Structure

The project currently contains two Python files:

```text
lead-management-cli/
│
├── main.py
├── leads.py
└── README.md
```

### `main.py`

Responsible for:

* Displaying the main menu
* Taking the user's menu choice
* Calling the appropriate function
* Running the main application loop
* Handling the program entry point

The main program starts here:

```python
if __name__ == "__main__":
    main()
```

---

### `leads.py`

Responsible for:

* Storing the lead data
* Adding leads
* Viewing leads
* Searching leads
* Updating lead status
* Deleting leads
* Calculating pipeline value
* Filtering by country
* Filtering by status

This keeps the lead-related functionality separate from the main menu.

---

# How the Application Works

The basic flow of the application is:

```text
Start Program
      ↓
main.py
      ↓
Display Menu
      ↓
User Selects Option
      ↓
Call Function From leads.py
      ↓
Perform Operation
      ↓
Return to Menu
      ↓
Repeat
      ↓
Exit
```

For example, when the user chooses:

```text
1. Add Lead
```

the flow becomes:

```text
main.py
   ↓
leads.add_lead()
   ↓
Ask for lead information
   ↓
Create dictionary
   ↓
Append dictionary to leads list
   ↓
Return to main menu
```

---

# Example Session

A typical session can look like:

```text
==================================================
              LEAD MANAGEMENT SYSTEM
==================================================
1. Add Lead
2. View All Leads
3. Search Leads
4. Update Lead Status
5. Delete Lead
6. Calculate Pipeline Value
7. Filter by Country
8. Filter by Status
9. Exit

Choose an option (1-9): 2
```

The application then displays the stored leads:

```text
==============================
Lead # 1
==============================

Name: Sarah Connor
Country: United States
Email: sarah.connor@cyberdyne.io
Status: New
Estimated Value: 4500.0
```

The user can then return to the menu and perform another operation.

---

# Current Limitations

This project is intentionally focused on **Python data structures and basic data processing**.

The lead data is currently stored only in memory.

That means:

```text
Start Program
      ↓
Load mock data
      ↓
Add / Update / Delete leads
      ↓
Work with data
      ↓
Close program
      ↓
Changes are lost
```

The application currently does not have persistent storage.

There is currently no:

* JSON storage
* CSV storage
* SQLite database
* Authentication
* API
* Web interface
* Cloud database
* User accounts

These are intentionally outside the scope of this project.

The purpose of this version is to understand how Python data structures can be used to build a small but functional application.

---

# Future Improvements

As my Python and backend skills progress, this project can be expanded.

Possible future improvements include:

* JSON file storage
* CSV import/export
* SQLite database
* Search by email
* More advanced search
* Lead sorting
* Sort by estimated value
* Lead priority
* Follow-up dates
* Lead notes
* More advanced pipeline analytics
* Lead conversion tracking
* REST API
* Web dashboard
* Authentication
* Database integration
* Cloud deployment

The current project provides the foundation for these future improvements.

---

# What I Learned

The biggest lesson from this project was learning how individual Python data structures can work together to represent real-world information.

Instead of learning lists and dictionaries only as isolated Python features, I used them together to build an actual application.

The core structure is:

```text
List
  ↓
Dictionary
  ↓
Key / Value Data
  ↓
Loops
  ↓
Conditions
  ↓
Searching
  ↓
Filtering
  ↓
Updating
  ↓
Deleting
  ↓
Data Processing
```

For example:

```python
leads = [
    {
        "name": "Sarah Connor",
        "country": "United States",
        "email": "sarah.connor@cyberdyne.io",
        "status": "New",
        "estimated_value": 4500.0
    }
]
```

This is a simple Python structure, but it represents a real-world concept: a collection of potential clients with business-related information.

---

# Project APEX — Week 3

This project is the final project of:

**Project APEX — Week 3: Python Data Structures**

The week focused on learning how Python's built-in data structures can be used to organize, manipulate, search, filter, and process data.

The progression was:

```text
Day 1 → Lists Fundamentals
Day 2 → Modifying Lists
Day 3 → Tuples + Sets
Day 4 → Dictionaries Fundamentals
Day 5 → Advanced Dictionaries + Data Processing
Day 6 → Lead Management CLI
```

The final project brought the week's concepts together into one practical application.

---

# Project Status

**Status: Completed ✅**

**Project APEX — Week 3: Completed ✅**

This project successfully applies Python lists, dictionaries, loops, conditions, list comprehensions, string methods, `enumerate()`, `sum()`, generator expressions, functions, and modules to build a functional command-line lead management system.

---

# Author

**Muhammad Sufyan**

Project APEX — Building toward becoming an **AI Software Engineer**.
