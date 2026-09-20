# Week 4 — Object-Oriented Programming (OOP)

## Overview

Week 4 focused on learning **Object-Oriented Programming (OOP)** in Python and applying it to a real-world project.

The goal was not to memorize OOP definitions, but to understand **when and why OOP improves code organization**.

The week progressed from basic classes and objects to designing and building a complete **Freelance CRM V2** using OOP principles.

---

# Main Learning Goal

Understand how to design Python applications using:

* Classes
* Objects
* Attributes
* Methods
* Constructors
* `self`
* Instance attributes
* Class attributes
* Encapsulation
* Dunder methods
* Dataclasses
* Inheritance
* Composition
* Object relationships
* Separation of models and application logic

A key rule throughout the week was:

> Do not turn every function into a class.

Classes should be used when they improve the organization and responsibility of the code.

---

# Day 1 — Classes, Objects & Attributes

## Topics Covered

* What classes solve
* Classes vs objects
* Creating classes
* Creating objects
* Attributes
* Instance attributes
* Accessing attributes
* Modifying attributes
* `self`
* Multiple objects
* Naming conventions

## Practice Entities

The following entities were used to understand OOP:

* Lead
* Client
* Project
* Invoice

Example concept:

```python
class Lead:
    pass
```

Creating an object:

```python
lead = Lead()
```

The main idea learned was:

```text
Class = blueprint
Object = actual instance
```

Multiple objects can be created from the same class while maintaining their own instance data.

---

# Day 2 — Constructors, Methods & Class Attributes

## Topics Covered

* `__init__`
* Constructors
* Why constructors are useful
* Initializing object data
* `self`
* Instance methods
* Method parameters
* Return values
* Methods that change object state
* Class attributes

Example:

```python
class Lead:
    source = "Website"

    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.status = "New"

    def mark_contacted(self):
        self.status = "Contacted"
```

The distinction between instance attributes and class attributes was practiced.

### Instance attribute

Belongs to an individual object:

```python
self.name
```

### Class attribute

Shared by instances unless overridden:

```python
source = "Website"
```

---

# Day 3 — Encapsulation, Dunder Methods & Dataclasses

## Encapsulation

Topics covered:

* Public attributes
* `_protected` naming convention
* `__private` naming convention
* Name mangling
* Why object state should sometimes be controlled
* Getters and setters
* `@property`
* Validation inside objects

The main idea was that an object should control important changes to its own state when necessary.

---

## Dunder Methods

The following special methods were studied:

```text
__init__
__str__
__repr__
__len__
__eq__
```

Examples of behavior:

```python
print(object)
```

uses:

```python
__str__
```

and:

```python
len(object)
```

can use:

```python
__len__
```

while:

```python
object1 == object2
```

can use:

```python
__eq__
```

---

## Dataclasses

Studied:

```python
from dataclasses import dataclass
```

and:

```python
@dataclass
class Lead:
    name: str
    email: str
```

Covered:

* Automatic `__init__`
* Type annotations
* Default values
* Methods inside dataclasses
* When dataclasses can reduce boilerplate

---

# Day 4 — Inheritance & Composition

## Inheritance

Topics covered:

* Parent classes
* Child classes
* Reusing attributes and methods
* Method overriding
* `super()`
* Parent initialization
* When inheritance makes sense
* When inheritance should not be used

Example relationship:

```text
Person
├── Client
└── Employee
```

The main mental model:

> Inheritance represents an **"is a"** relationship.

For example:

```text
Client IS A Person
Employee IS A Person
```

---

## Composition

Composition was studied as an important relationship for the CRM.

The main mental model:

> Composition represents a **"has a"** relationship.

CRM example:

```text
Client
├── Project
├── Project
└── Project
```

and:

```text
Project
├── Invoice
├── Invoice
└── Invoice
```

Therefore:

```text
Client HAS Projects
Project HAS Invoices
```

Composition was implemented using object references and lists of objects.

---

# Day 5 — OOP Design + CRM V2 Architecture

Day 5 focused on designing the application before building the complete CLI.

The four core entities were defined:

```text
Lead
Client
Project
Invoice
```

---

## Lead

### Data

```text
name
email
country
estimated_value
status
```

### Behaviors

```text
mark_contacted()
qualify()
convert_to_client()
is_high_value()
```

---

## Client

### Data

```text
name
email
country
projects
```

### Behaviors

```text
add_project()
get_projects()
get_total_revenue()
get_history()
```

---

## Project

### Data

```text
name
client
budget
status
invoices
```

### Behaviors

```text
update_status()
add_invoice()
get_total_invoiced()
get_outstanding()
```

---

## Invoice

### Data

```text
invoice_id
amount
status
```

### Behaviors

```text
mark_paid()
mark_unpaid()
is_outstanding()
```

---

# CRM Relationships

The main object relationship was designed as:

```text
Lead
 │
 │ convert
 ▼
Client
 │
 ├── Project
 │    ├── Invoice
 │    └── Invoice
 │
 └── Project
      └── Invoice
```

The important relationships are:

```text
Lead → Client
Client → Projects
Project → Invoices
```

---

# Application Architecture

The project was organized into separate models and services:

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

The main architectural principle was:

> Separate models from application logic.

### Models

Define what the entities are and what they can do.

### Services

Manage application-level operations involving multiple objects.

### `main.py`

Handles application interaction and the CLI.

---

# Day 6 — Weekly Project

## Freelance CRM V2

The final project applied the OOP concepts from the entire week.

The project replaced the dictionary-based Lead Management CLI from Week 3 with an object-oriented design.

---

# Features Implemented

## 1. Lead Management

The CRM supports:

* Add Lead
* View Leads
* Search Lead
* Update Lead
* Delete Lead

Leads are now represented using the `Lead` class rather than dictionaries.

---

## 2. Lead → Client Conversion

Qualified leads can be converted into Client objects.

The relationship is:

```text
Lead
 ↓
convert_to_client()
 ↓
Client
```

The converted client is then managed by the CRM.

---

## 3. Project Management

Clients can have multiple projects.

Example:

```text
Client
├── E-commerce Website
├── Mobile App
└── AI Chatbot
```

This uses composition:

```text
Client
└── projects[]
```

---

## 4. Project Status

Projects support statuses including:

```text
Planning
In Progress
Completed
Cancelled
```

Project status can be updated through the Project object's behavior.

---

## 5. Invoice Management

Projects can contain multiple invoices.

Example:

```text
E-commerce Website

Invoice #001 → $1,000 → Paid
Invoice #002 → $1,000 → Unpaid
```

The relationship is:

```text
Project
└── invoices[]
```

---

## 6. Revenue Tracking

The CRM calculates:

```text
Total Invoiced
Paid Revenue
Outstanding Revenue
```

Example:

```text
Total Invoiced:      $5,000
Paid Revenue:        $3,000
Outstanding Revenue: $2,000
```

Revenue calculations are handled by the relevant objects rather than being placed entirely inside the CLI.

---

## 7. Client History

The CRM can display a client's projects, project statuses, revenue, and invoices.

Example structure:

```text
CLIENT HISTORY

Client: Sarah Connor

Projects:

1. E-commerce Website
   Status: Completed
   Revenue: $2,500

2. AI Chatbot
   Status: In Progress
   Revenue: $4,000

Invoices:
INV-001   $2,500   Paid
INV-002   $2,000   Paid
INV-003   $2,000   Unpaid
```

---

# OOP Concepts Applied in the Project

The project applied:

* Classes
* Objects
* Constructors
* Instance attributes
* Class attributes
* Instance methods
* Encapsulation
* Dunder methods
* Inheritance concepts
* Composition
* Object relationships
* Separation of responsibilities

The most important OOP design used in the project was composition:

```text
Client
 └── Projects
      └── Invoices
```

---

# From Week 3 to Week 4

The Week 3 project used dictionary-based data:

```python
lead["name"]
lead["status"]
lead["estimated_value"]
```

Week 4 moved to objects:

```python
lead.name
lead.status
lead.estimated_value
```

Behavior also moved into the objects.

Instead of external operations such as:

```python
mark_contacted(lead)
```

the object now owns the behavior:

```python
lead.mark_contacted()
```

Similarly:

```python
lead.qualify()
lead.convert_to_client()
client.add_project(project)
project.add_invoice(invoice)
invoice.mark_paid()
```

This represents the transition from procedural data handling toward object-oriented application design.

---

# Week 4 Key Lessons

## 1. Classes should have responsibilities

An object should own data and behavior that naturally belong together.

## 2. Not everything needs to be a class

OOP should be used when it improves organization and design.

## 3. Inheritance means "is a"

```text
Person
├── Client
└── Employee
```

## 4. Composition means "has a"

```text
Client
└── Project
    └── Invoice
```

## 5. Objects should work together

The CRM demonstrates:

```text
Lead
 ↓
Client
 ↓
Project
 ↓
Invoice
```

## 6. Separate responsibilities

The architecture separates:

```text
Models
Services
CLI
```

This makes the application easier to understand and extend.

---

# Week 4 Outcome

By the end of Week 4, the following progression was completed:

```text
Classes
   ↓
Objects
   ↓
Attributes
   ↓
Methods
   ↓
Encapsulation
   ↓
Dunder Methods
   ↓
Dataclasses
   ↓
Inheritance
   ↓
Composition
   ↓
OOP Design
   ↓
CRM Architecture
   ↓
Freelance CRM V2
```

The main outcome of the week was learning how to use OOP to organize a multi-entity application rather than simply learning isolated OOP syntax.
