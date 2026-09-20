# Freelance CRM V2

A command-line Customer Relationship Management (CRM) application built with Python using Object-Oriented Programming (OOP).

The project manages leads, converts qualified leads into clients, assigns projects to clients, creates invoices, tracks invoice payments, and displays client history.

---

## Project Status

**Completed**

This project was built as the Week 4 project for practicing Python Object-Oriented Programming.

---

## Features

### Lead Management

* Add leads
* View all leads
* Search leads by name or email
* Update lead status
* Delete leads
* Convert qualified leads into clients

### Client Management

* View all clients
* Track client projects
* Track total invoiced revenue
* Track paid revenue
* Track outstanding revenue
* View complete client history

### Project Management

* Add projects to clients
* Store project budgets
* Update project status
* Track project invoices
* Calculate total invoiced amount
* Calculate paid revenue
* Calculate outstanding revenue

### Invoice Management

* Create invoices
* Store invoice ID and amount
* Mark invoices as paid
* Track unpaid invoices
* Calculate outstanding revenue

---

## CLI Menu

The application provides the following menu:

```text
========================================
       FREELANCE CRM V2
========================================

1. Add Lead
2. View Leads
3. Search Lead
4. Update Lead
5. Delete Lead
6. Convert Lead
7. View Clients
8. Add Project
9. Update Project Status
10. Create Invoice
11. Mark Invoice Paid
12. Client History
13. Exit
```

---

## Project Structure

```text
freelance_crm_v2/
│
├── main.py
│
├── models/
│   ├── __init__.py
│   ├── lead.py
│   ├── client.py
│   ├── project.py
│   └── invoice.py
│
├── services/
│   ├── __init__.py
│   └── crm.py
│
└── README.md
```

---

## Architecture

The project separates responsibilities into different parts.

```text
main.py
   │
   ▼
CRMService
   │
   ├── Leads
   ├── Clients
   ├── Projects
   └── Invoices
        │
        ▼
      Models
```

### `main.py`

Responsible for the command-line interface.

It handles:

* Displaying the menu
* Getting user input
* Displaying information
* Calling CRM service operations
* Basic input validation
* Navigating between CRM features

The CLI does not directly manage the application's main data collections.

---

### `services/crm.py`

Contains the `CRMService` class.

The service manages:

* Lead collection
* Client collection
* Adding leads
* Searching leads
* Updating lead status
* Deleting leads
* Converting leads into clients
* Creating projects
* Creating invoices

---

### `models/lead.py`

Contains the `Lead` class.

A lead contains:

```text
name
email
country
estimated_value
status
```

A new lead starts with:

```text
status = "New"
```

The class provides methods for:

* Marking a lead as contacted
* Qualifying a lead
* Checking whether a lead is high value
* Converting a qualified lead into a client

A lead can only be converted when its status is:

```text
Qualified
```

---

### `models/client.py`

Contains the `Client` class.

A client contains:

```text
name
email
country
projects
```

Each client maintains a list of projects.

The class provides methods for:

* Adding projects
* Getting projects
* Calculating total invoiced revenue
* Calculating paid revenue
* Calculating outstanding revenue
* Building client history

This demonstrates **composition**, because a `Client` contains multiple `Project` objects.

---

### `models/project.py`

Contains the `Project` class.

A project contains:

```text
name
budget
client
status
invoices
```

A new project starts with:

```text
status = "Planning"
```

Valid project statuses are:

```text
Planning
In Progress
Completed
Cancelled
```

The class provides methods for:

* Updating project status
* Adding invoices
* Calculating total invoiced revenue
* Calculating paid revenue
* Calculating outstanding revenue

A project maintains a list of invoices.

---

### `models/invoice.py`

Contains the `Invoice` class.

An invoice contains:

```text
invoice_id
amount
status
```

A new invoice starts with:

```text
status = "Unpaid"
```

The class provides methods for:

* Marking an invoice as paid
* Marking an invoice as unpaid
* Checking whether an invoice is outstanding

The invoice amount uses a property with validation to prevent negative values.

---

## OOP Concepts Practiced

This project applies the following Object-Oriented Programming concepts.

### Classes and Objects

The application uses classes for:

```text
Lead
Client
Project
Invoice
CRMService
```

Objects are created from these classes while the application is running.

---

### Instance Attributes

Objects maintain their own data.

For example, a `Lead` stores:

```python
self.name
self.email
self.country
self.estimated_value
self.status
```

---

### Instance Methods

The model classes contain methods that operate on their own data.

Examples:

```python
lead.mark_contacted()
```

```python
project.update_status("Completed")
```

```python
invoice.mark_paid()
```

---

### Constructors

Each model uses `__init__()` to initialize object data.

Example:

```python
def __init__(self, name, email, country, estimated_value):
    self.name = name
    self.email = email
    self.country = country
    self.estimated_value = estimated_value
    self.status = "New"
```

---

### `self`

The project uses `self` to access instance attributes and methods belonging to the current object.

---

### Encapsulation

The project uses properties for controlled access and validation.

For example, `Invoice.amount` internally uses:

```python
self._amount
```

and exposes the value through:

```python
@property
def amount(self):
    return self._amount
```

The setter prevents negative invoice amounts.

The `Project.budget` property also prevents negative values.

---

### Composition

Composition is one of the main OOP concepts demonstrated in this project.

The relationship is:

```text
Client
  │
  └── Projects
        │
        └── Invoices
```

A client contains projects, and a project contains invoices.

For example:

```python
client.projects
```

and:

```python
project.invoices
```

---

### Dunder Methods

The project implements `__str__()` in the model classes to provide readable object representations.

Examples include:

```python
str(lead)
str(client)
str(project)
str(invoice)
```

---

### Class Attributes

`Project` uses a class attribute to define valid project statuses:

```python
VALID_STATUSES = {
    "Planning",
    "In Progress",
    "Completed",
    "Cancelled"
}
```

---

## Data Flow

The main CRM workflow is:

```text
Lead
 │
 │ Qualified
 ▼
Client
 │
 │ Add Project
 ▼
Project
 │
 │ Create Invoice
 ▼
Invoice
 │
 ├── Unpaid
 │
 └── Paid
```

---

## Lead Conversion Flow

A lead starts as:

```text
New
```

It can be changed to:

```text
Contacted
```

and then:

```text
Qualified
```

Only a qualified lead can be converted into a client.

```text
New
 ↓
Contacted
 ↓
Qualified
 ↓
Client
```

When conversion happens, the lead is removed from the CRM's lead list and the resulting client is added to the client list.

---

## Revenue Tracking

The project tracks three revenue values.

### Total Invoiced Revenue

The sum of all invoices belonging to a client's projects.

```text
Total Invoiced
=
All Invoice Amounts
```

### Paid Revenue

The sum of invoices whose status is:

```text
Paid
```

### Outstanding Revenue

The sum of invoices whose status is:

```text
Unpaid
```

The relationship is:

```text
Total Invoiced
=
Paid Revenue
+
Outstanding Revenue
```

---

## Validation

The project includes validation for several inputs.

### Invoice Amount

Negative invoice amounts are rejected.

```text
Amount < 0
```

is invalid.

### Project Budget

Negative project budgets are rejected.

### Lead Estimated Value

The CLI prevents negative values when entering a lead's estimated value.

### Project Status

Only the following project statuses are accepted:

```text
Planning
In Progress
Completed
Cancelled
```

### Lead Status

The CRM service accepts:

```text
New
Contacted
Qualified
```

---

## Technologies Used

* Python 3
* Object-Oriented Programming
* Python classes and objects
* Properties
* Encapsulation
* Composition
* Dunder methods
* Command-Line Interface (CLI)

No external Python packages are required.

---

## How to Run

Open the terminal inside the project folder:

```bash
cd freelance_crm_v2
```

Run:

```bash
python main.py
```

---

## Example Workflow

A typical workflow can be:

```text
1. Add Lead
      ↓
2. Update Lead
      ↓
3. Change status to Qualified
      ↓
4. Convert Lead
      ↓
5. View Clients
      ↓
6. Add Project
      ↓
7. Create Invoice
      ↓
8. Mark Invoice Paid
      ↓
9. View Client History
```

---

## Data Storage

The application currently stores all data **in memory** using Python lists.

The CRM service maintains:

```python
self.leads = []
self.clients = []
```

Projects are stored inside clients, and invoices are stored inside projects.

There is currently:

* No database
* No JSON file storage
* No CSV storage
* No external API
* No persistent storage

Therefore, all data is lost when the program exits.

---

## Current Limitations

* Data is not persistent.
* There is no database.
* There is no authentication.
* There is no multi-user support.
* There is no GUI.
* There is no web interface.
* Invoice IDs are entered manually.
* Client and project data exists only during the current program session.

---

## Purpose of the Project

The main purpose of this project is to practice applying Object-Oriented Programming to a multi-component Python application.

The project focuses on organizing code into:

```text
Models
Services
CLI
```

instead of keeping the entire application inside a single file.

---

## Learning Outcomes

By completing this project, the following concepts were practiced:

* Designing classes
* Creating objects
* Using constructors
* Using instance attributes
* Using instance methods
* Using `self`
* Using class attributes
* Encapsulation
* Properties and setters
* Input validation
* Composition
* Working with multiple related objects
* Using dunder methods
* Separating models from business logic
* Separating the CLI from application logic
* Organizing a Python project into packages and modules
* Building a complete CLI application with OOP
