# Freelance CRM V3

A command-line freelance CRM built with Python.

This project started as the Week 4 Freelance CRM and was extended in Week 5 with persistent JSON storage, serialization and deserialization, exception handling, and backups before destructive operations.

The purpose of this project is to practice how an object-oriented Python application can store and restore its data instead of keeping everything only in memory.

---

## Features

### Lead Management

* Add Lead
* View Leads
* Search Lead
* Update Lead
* Delete Lead
* Convert Lead to Client

### Client Management

* View Clients
* View Client History

### Project Management

* Add Project
* Update Project Status

### Invoice Management

* Create Invoice
* Mark Invoice Paid

### Persistent Storage

CRM data is stored in:

```text
data/crm.json
```

The application loads the saved CRM data when it starts and saves successful changes to the JSON file.

### Backups

Before deleting a lead, the application creates a backup of the current CRM data.

Backups are stored in:

```text
data/backups/
```

Backup files use timestamped filenames.

### Error Handling

The application handles expected storage-related problems such as:

* Missing `crm.json`
* Invalid JSON
* Storage errors
* Backup failures
* Invalid data

---

## Menu

The application provides the following menu:

```text
1.  Add Lead
2.  View Leads
3.  Search Lead
4.  Update Lead
5.  Delete Lead
6.  Convert Lead
7.  View Clients
8.  Add Project
9.  Update Project Status
10. Create Invoice
11. Mark Invoice Paid
12. Client History
13. Exit
```

---

## Project Structure

```text
freelance_crm_v3/
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
│   └── crm.py
│
├── storage/
│   ├── serializers.py
│   └── json_storage.py
│
├── utils/
│   ├── validators.py
│   └── exceptions.py
│
├── data/
│   ├── crm.json
│   └── backups/
│
└── README.md
```

---

# Architecture

The application separates user interaction, CRM logic, models, and storage.

```text
                    main.py
                       │
                       ▼
                 CRMService
                       │
              ┌────────┴────────┐
              ▼                 ▼
           Models          JsonStorage
              │                 │
              │                 ▼
              │          serializers.py
              │                 │
              │                 ▼
              │             crm.json
              │
              └── In-memory CRM state
```

The main components have different responsibilities.

---

## `main.py`

`main.py` is the command-line interface.

It handles:

* Showing the menu
* Getting user input
* Validating user input through helper functions
* Displaying information
* Selecting leads, clients, projects, and invoices
* Calling operations on `CRMService`

`main.py` is responsible for interaction with the user rather than storing the CRM state itself.

---

## `models/`

The `models` package contains the main objects used by the CRM.

### `lead.py`

Contains the `Lead` model.

A lead contains information such as:

* ID
* Name
* Email
* Country
* Estimated value
* Status

The model also contains lead-related behavior such as changing its status and converting a lead into a client.

### `client.py`

Contains the `Client` model.

A client contains:

* ID
* Name
* Email
* Country
* Projects

A client owns its projects through its `projects` list.

### `project.py`

Contains the `Project` model.

A project contains:

* ID
* Name
* Budget
* Client
* Status
* Invoices

A project belongs to a client and contains its invoices.

### `invoice.py`

Contains the `Invoice` model.

An invoice contains:

* ID
* Amount
* Status

An invoice belongs to a project.

---

# In-Memory Relationships

The CRM uses object relationships while the application is running.

The structure is:

```text
CRMService
│
├── leads
│
└── clients
     │
     └── Client
          │
          └── projects
               │
               └── Project
                    │
                    └── invoices
                         │
                         └── Invoice
```

For example:

```text
Client
  └── Project
       └── Invoice
```

The `CRMService` keeps the main collections:

```python
self.leads
self.clients
```

Projects belong to clients, and invoices belong to projects.

The service does not maintain separate top-level project and invoice collections.

---

# `services/crm.py`

`CRMService` contains the application's CRM operations and manages the in-memory CRM state.

It is responsible for operations such as:

* Adding leads
* Searching leads
* Updating leads
* Deleting leads
* Converting leads
* Adding projects
* Updating project status
* Adding invoices
* Marking invoices as paid
* Loading CRM data
* Saving CRM data
* Creating backups through the storage layer

The service acts as the main application layer between the command-line interface and the underlying models/storage system.

---

# `storage/`

The `storage` package handles persistence.

It contains two important parts:

```text
storage/
├── serializers.py
└── json_storage.py
```

## `serializers.py`

The serializers convert Python objects into JSON-compatible dictionaries and convert dictionaries back into Python objects.

### Serialization

Python objects are converted into dictionaries before saving.

```text
Python objects
      ↓
Serializer
      ↓
Dictionaries
```

### Deserialization

Saved dictionaries are converted back into Python objects when loading.

```text
Dictionaries
      ↓
Deserializer
      ↓
Python objects
```

The serializer also reconstructs the relationships between:

```text
Client → Project → Invoice
```

using IDs stored in the JSON data.

---

## `json_storage.py`

`JsonStorage` handles the actual JSON file operations.

It is responsible for:

* Creating required directories
* Loading `crm.json`
* Saving data to `crm.json`
* Creating an empty CRM data structure when the file does not exist
* Creating backups
* Raising storage-related exceptions when operations fail

The storage layer does not manage the CRM's business objects directly.

It works with JSON-compatible data provided by the serialization layer.

---

# `utils/`

The `utils` package contains supporting functionality.

## `validators.py`

Contains input validation functions used by the application.

## `exceptions.py`

Contains application-specific exceptions used to represent expected problems such as:

* Invalid stored data
* Backup failures

---

# Data Storage

The main CRM data is stored in:

```text
data/crm.json
```

The JSON file contains four main sections:

```json
{
    "leads": [],
    "clients": [],
    "projects": [],
    "invoices": []
}
```

The actual arrays contain the saved CRM records.

Relationships between objects are represented using IDs.

For example, a project stores the ID of its client:

```json
{
    "id": "P001",
    "name": "Website",
    "client_id": "C001",
    "budget": 2000,
    "status": "Planning",
    "invoice_ids": []
}
```

An invoice stores the ID of its project:

```json
{
    "id": "I001",
    "amount": 2000,
    "status": "Unpaid",
    "project_id": "P001"
}
```

This allows the application to store the relationships in JSON and reconstruct the Python object relationships when the application starts.

---

# Save Flow

When CRM data is saved:

```text
CRM objects
     ↓
crm_to_dict()
     ↓
Dictionaries
     ↓
JsonStorage
     ↓
json.dump()
     ↓
data/crm.json
```

The objects are not written directly to JSON.

They are first converted into JSON-compatible dictionaries.

---

# Load Flow

When the application starts:

```text
data/crm.json
     ↓
json.load()
     ↓
Dictionaries
     ↓
crm_from_dict()
     ↓
Python objects
     ↓
CRMService
```

During deserialization, the application reconstructs relationships between clients, projects, and invoices.

---

# Application Startup

The application starts by creating the storage and CRM service:

```text
Start
  ↓
Create storage
  ↓
Create CRMService
  ↓
Load saved data
  ↓
Restore Python objects
  ↓
Show menu
```

If `data/crm.json` does not exist, the storage layer creates an empty CRM data structure and saves it.

The application can therefore start with an empty CRM.

---

# Saving Changes

Successful state-changing operations save the updated CRM state.

Examples include:

```text
Add Lead
Update Lead
Convert Lead
Add Project
Update Project Status
Create Invoice
Mark Invoice Paid
```

The general process is:

```text
User action
     ↓
CRMService operation
     ↓
Change in-memory objects
     ↓
Serialize CRM data
     ↓
Save crm.json
```

This means changes are persisted during the application instead of existing only until the program closes.

---

# Safe Deletion

Deletion is treated differently because it removes existing data.

Before deleting a lead, the application creates a backup of the current CRM file.

The process is:

```text
Delete request
     ↓
Check target
     ↓
Create backup
     ↓
Backup succeeds?
     │
     ├── No → deletion stops
     │
     └── Yes
           ↓
       Delete lead
           ↓
       Save new CRM state
```

The important rule is:

> The backup must be created before the deletion.

This ensures the backup represents the CRM state before the destructive change.

If backup creation fails, the deletion does not continue.

---

# Backups

Backups are stored in:

```text
data/backups/
```

Example:

```text
data/
├── crm.json
└── backups/
    ├── crm_backup_20260930_182010.json
    ├── crm_backup_20260930_183542.json
    └── ...
```

Each backup contains a copy of the CRM data from before the destructive operation.

Backups are created using `shutil.copy2()` and timestamped filenames.

---

# Missing Files and Directories

The application creates the required directories automatically.

For example:

```text
data/
data/backups/
```

If `crm.json` does not exist, the storage layer creates an empty CRM structure:

```json
{
    "leads": [],
    "clients": [],
    "projects": [],
    "invoices": []
}
```

This allows the application to start without an existing CRM data file.

---

# Invalid JSON

A JSON file can exist while containing invalid JSON.

For example:

```text
{this is not valid json
```

When this happens, `json.load()` raises a `JSONDecodeError`.

The storage layer catches this error and raises an application-specific `InvalidDataError`.

The existing CRM data is not silently replaced with an empty CRM.

---

# Project Flow

## Startup

```text
main.py
   ↓
JsonStorage
   ↓
load crm.json
   ↓
crm_from_dict()
   ↓
Python objects
   ↓
CRMService
   ↓
CLI menu
```

## Add / Update

```text
main.py
   ↓
CRMService
   ↓
Model changes
   ↓
crm_to_dict()
   ↓
JsonStorage
   ↓
crm.json
```

## Delete Lead

```text
main.py
   ↓
CRMService.delete_lead()
   ↓
Create backup
   ↓
Delete lead
   ↓
Save
```

---

# Technology

* Python
* Object-Oriented Programming
* Command-Line Interface
* `pathlib`
* JSON
* File Handling
* Serialization
* Deserialization
* Exception Handling
* `shutil`
* Persistent Storage

---

# What This Project Demonstrates

Freelance CRM V3 demonstrates how a Python application can evolve from an in-memory program into a persistent application.

The project combines:

```text
Object-Oriented Programming
        +
File Handling
        +
pathlib
        +
JSON
        +
Serialization
        +
Deserialization
        +
Exception Handling
        +
Persistent Storage
        +
Backups
```

The main goal is not only to use these Python features individually, but to understand how they work together inside an application.

---

# Project Progression

## Week 4 — Freelance CRM V2

The previous version focused on:

```text
OOP
Models
Classes and Objects
Methods
Encapsulation
Composition
Relationships
CRM Operations
```

The CRM existed primarily as an in-memory application.

---

## Week 5 — Freelance CRM V3

The project was extended with:

```text
File Handling
pathlib
JSON
Serialization
Deserialization
Persistent Storage
Exception Handling
Storage Layer
Backups
```

The result is a CRM that can save its state to disk and restore it when the application starts again.

---

# Current Scope

Freelance CRM V3 currently focuses on:

```text
Lead Management
Client Management
Project Management
Invoice Management
Object Relationships
Persistent JSON Storage
Serialization / Deserialization
Exception Handling
Backup Before Lead Deletion
```

The project is a learning project focused on understanding application architecture and persistence in Python.
