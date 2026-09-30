# Week 5 — Files, JSON, Exceptions & CRM Persistence

## Overview

Week 5 focused on moving the Freelance CRM from an in-memory application toward a persistent and safer application.

The week covered:

* File handling
* `pathlib`
* JSON and serialization
* Exception handling
* CRM persistence architecture
* Backups and safe destructive operations

The main goal was not only to learn individual Python features, but to understand how these features work together inside a real application.

---

## Day 1 — File Handling Fundamentals

### Topics

* `open()`
* File modes:

  * `"r"` — read
  * `"w"` — write
  * `"a"` — append
  * `"x"` — create
* `encoding="utf-8"`
* `.read()`
* `.readline()`
* `.readlines()`
* `.write()`
* `.writelines()`
* Context managers
* `with open(...)`
* Relative paths
* Absolute paths
* Current working directory
* `FileNotFoundError`

### Practice

Created small programs to:

* Create a text file
* Write content
* Read content
* Append content
* Handle a missing file

### Mini Project

Built a simple CRM Activity Log using a file to store activities.

### Key Principle

> First understand files separately before connecting them to the CRM.

---

## Day 2 — `pathlib` & File System Management

### Topics

```python
from pathlib import Path
```

Learned:

* `Path()`
* Building paths with `/`
* `.exists()`
* `.is_file()`
* `.is_dir()`
* `.mkdir()`
* `.iterdir()`
* `.parent`
* `.name`
* `.suffix`
* `Path.cwd()`
* `read_text()`
* `write_text()`
* `path.open()`

Also learned:

```python
mkdir(parents=True, exist_ok=True)
```

and understood the purpose of:

* `parents=True`
* `exist_ok=True`

### Practice

Built a Data Directory Manager to:

* Check whether `data/` exists
* Create missing directories
* Create `backups/`
* Check whether `crm.json` exists
* Inspect file and directory information

### Key Principle

> `pathlib` becomes the standard way of managing paths in the project.

---

## Day 3 — JSON & Serialization

### Topics

* What JSON is
* Python dictionaries vs JSON
* JSON objects and arrays
* JSON-supported data types
* `json.dump()`
* `json.load()`
* `json.dumps()`
* `json.loads()`
* Serialization
* Deserialization
* `indent=4`

### Python → JSON

Learned how:

```text
dict   → object
list   → array
str    → string
int    → number
float  → number
True   → true
False  → false
None   → null
```

### Practice Project

Built Lead JSON Storage.

Python lead data was converted into JSON, saved to a file, and loaded back into Python.

### Key Principle

> JSON is a data-storage format and a bridge between Python data and persistent storage.

---

## Day 4 — Exception Handling

### Topics

* Why exceptions exist
* `try`
* `except`
* Multiple `except` blocks
* `except ... as error`
* `else`
* `finally`
* `raise`
* Custom exceptions
* Exception propagation
* Specific exception handling
* Avoiding overly broad exceptions

### Important Exceptions

* `ValueError`
* `TypeError`
* `FileNotFoundError`
* `FileExistsError`
* `KeyError`
* `IndexError`
* `ZeroDivisionError`
* `JSONDecodeError`

### Custom Exceptions

Learned how to create application-specific exceptions such as:

```python
class LeadNotFoundError(Exception):
    pass
```

### Mini Project

Built a Safe JSON Loader capable of handling:

* Missing files
* Invalid JSON
* Unexpected data

### Key Principle

> Don't use exceptions to hide problems. Use them to handle expected failures safely.

---

## Day 5 & 6 — CRM Persistence Architecture

Day 5 was intentionally given extra time because architecture was the most difficult part of the week.

### Time Spent

**2 days**

The focus was understanding the architecture before implementing it.

### Main Architecture

```text
Application
     ↓
CRM Service
     ↓
Storage
     ↓
JSON File
```

### Learned the Responsibilities of Each Layer

#### `main.py`

Handles:

* User interaction
* Menu
* Input
* Output

#### Models

Represent:

* Lead
* Client
* Project
* Invoice

#### CRM Service

Handles:

* CRM operations
* Business logic
* In-memory CRM state

#### Storage

Handles:

* File paths
* JSON loading
* JSON saving
* Persistent data
* Backups

#### Data

Contains persistent CRM data.

### Serialization Flow

```text
Python object
     ↓
dictionary
     ↓
JSON
     ↓
file
```

### Deserialization Flow

```text
file
     ↓
JSON
     ↓
dictionary
     ↓
Python object
```

### Startup Flow

```text
Start application
      ↓
Prepare data directories
      ↓
Load crm.json
      ↓
Convert stored data back into Python objects
      ↓
CRM becomes ready
      ↓
Show menu
```

### Mutation Flow

```text
User action
      ↓
CRM changes
      ↓
Serialize data
      ↓
Save JSON
```

### Key Principle

> Don't just make JSON work. Understand where persistence belongs in the architecture.

---

## Day 7 - 10 — Backups, Safe Destructive Changes & CRM V3

Day 7 was the final integration and project-building phase.

### Time Spent

**4 days**

These four days were used to understand the complete flow, wire the architecture together, implement the persistence system, and test the final CRM.

### Backup System

Created a backup system for the existing CRM data.

Structure:

```text
data/
├── crm.json
└── backups/
    ├── crm_backup_....json
    ├── crm_backup_....json
    └── ...
```

Backups are created before destructive operations.

### Destructive Operations

The project protects data before:

* Delete Lead

In future, can also add:

* Delete Client
* Delete Project
* Delete Invoice

The flow is:

```text
Validate target
      ↓
Create backup
      ↓
Perform deletion
      ↓
Save new CRM state
```

### Missing Data Handling

The application handles:

* Missing `data/` directory
* Missing `backups/` directory
* Missing `crm.json`

Missing CRM data can result in an empty/default CRM state instead of an application crash.

### Corrupted JSON

The application detects invalid JSON instead of silently replacing it with empty data.

### Persistence Testing

Tested that:

* Added leads remain after restarting
* Updated data remains after restarting
* Clients, projects, and invoices persist
* Deleted records are removed from current state
* Backups are created before destructive changes
* Missing directories are recreated
* Missing JSON is handled safely
* Invalid JSON is detected

### Key Principle

> Never destroy the only copy of important data.

---

# Week 5 Final Outcome

At the beginning of Week 5, the CRM primarily stored its state in memory.

By the end of the week, the CRM had a persistence and reliability system based on:

```text
Python Objects
      ↓
Serialization
      ↓
JSON
      ↓
crm.json
```

and:

```text
Destructive operation
      ↓
Backup
      ↓
Change
      ↓
Save
```

The week connected several previously separate Python concepts into one working application architecture.

---

**6 learning sections completed over approximately 10 days.**

The additional time was mainly spent understanding architecture and building the final project rather than rushing through the material.
