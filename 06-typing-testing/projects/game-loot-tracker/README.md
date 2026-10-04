# 🎮 Game Loot Tracker

A small command-line Python application for managing game loot.

This project was created as a practice project for **Python type hints and clean code fundamentals**.

The application allows the user to add loot, view inventory, search for loot, find rare loot, calculate total inventory value, and remove loot.

---

## Features

### Add Loot

Add a new loot item by providing:

* Name
* Rarity
* Value

Supported rarities:

* Common
* Rare
* Epic
* Legendary

Each loot item receives an automatically generated ID:

```text
L001
L002
L003
```

---

### View Inventory

Displays all loot currently stored in the inventory.

Example:

```text
ID: L001 | Name: Dragon Sword | Rarity: Legendary | Value: $5000.00
```

---

### Search Loot

Search for loot by name.

The search checks whether the entered search text appears inside the loot name.

Example:

```text
Search: sword
```

can find:

```text
Dragon Sword
```

If no matching loot is found, the application displays:

```text
No loot found matching your query!
```

---

### Show Rare Loot

Displays loot with the following rarities:

```text
Epic
Legendary
```

If no rare loot exists, the application displays:

```text
No rare loot found!
```

---

### Show Inventory Value

Calculates the total value of all loot currently in the inventory.

Example:

```text
Total inventory value: $6850.0
```

---

### Remove Loot

Displays the inventory and allows the user to remove an item by its **position number**.

For example:

```text
Choose by number (1): 2
```

The selected item is removed from the inventory.

---

## Project Structure

```text
game_loot_tracker/
│
├── main.py
├── validators.py
├── loot.py
└── loot_service.py
```

---

## File Responsibilities

### `main.py`

Handles the command-line interface.

It contains:

* Main menu
* User input
* Menu selection
* Calling the appropriate `LootService` methods
* Displaying results and errors

The menu contains:

```text
1. Add Loot
2. View Inventory
3. Search Loot
4. Show Rare Loot
5. Show Inventory Value
6. Remove Loot
7. Exit
```

---

### `loot.py`

Contains the `Loot` class.

Each `Loot` object stores:

```text
id
name
rarity
value
```

The class also provides a string representation used when displaying loot.

---

### `loot_service.py`

Contains the `LootService` class.

`LootService` manages the loot collection and provides methods for:

* Adding loot
* Viewing inventory
* Searching loot
* Finding rare loot
* Calculating inventory value
* Removing loot

The loot is stored in memory using a list:

```python
self.loots: list[Loot] = []
```

The project does not currently save loot to a file or database.

---

### `validators.py`

Contains validation functions for:

* Loot names
* Numeric values
* Loot rarity

The supported rarities are:

```text
Common
Rare
Epic
Legendary
```

---

## Data Storage

The application currently stores all loot **in memory**.

When the program starts:

```text
LootService
    ↓
Empty loot list
```

Loot is added to the list while the program is running.

There is currently:

* No JSON storage
* No database
* No file persistence
* No backup system

Therefore, all loot is lost when the program exits.

---

## Type Hints

Type hints are used throughout important parts of the project.

Examples include:

```python
def add_loot(
    self,
    name: str,
    rarity: str,
    value: float
) -> Loot:
```

```python
self.loots: list[Loot] = []
```

```python
def rare_loot(self) -> list[Loot]:
```

```python
def inventory_value(self) -> float:
```

The project uses Python's modern type hint syntax such as:

```python
list[Loot]
float
str
float | int
```

---

## Validation

The project validates:

### Name

A loot name cannot be empty or blank.

### Value

The value cannot be negative.

### Rarity

The rarity must match one of the supported rarity values.

Invalid input raises `ValueError`, which is handled by the command-line interface.

---

## Error Handling

The application handles invalid user input using `try` / `except`.

For example, invalid numeric input when selecting a menu option is handled without crashing the application.

Validation errors are also displayed to the user.

---

## Application Flow

The basic flow of the application is:

```text
User
  ↓
main.py
  ↓
LootService
  ↓
Validators
  ↓
Loot
```

For example, when adding loot:

```text
User enters loot information
        ↓
main.py
        ↓
LootService.add_loot()
        ↓
Validate name
        ↓
Validate rarity
        ↓
Validate value
        ↓
Create Loot object
        ↓
Add Loot object to inventory
```

---

## Technologies

* Python
* Object-Oriented Programming
* Functions
* Classes
* Lists
* Dictionaries/Sets
* Type Hints
* Input Validation
* Exception Handling
* Command-Line Interface

---

## Purpose of the Project

This is a small practice project from **Project APEX Week 6**.

The main purpose is to practice:

* Function parameter type hints
* Return type hints
* Collection type hints
* Type aliases
* Clear naming
* Small functions
* Avoiding unnecessary duplication
* Constants
* Basic validation
* Docstrings
* Separating responsibilities

The project is intentionally small and does not use persistent storage or advanced architecture.

---

## Current Limitations

The current version has the following limitations:

* Loot is only stored in memory.
* Loot is lost when the application exits.
* Loot is removed using its inventory position rather than its generated ID.
* The project does not have automated tests.
* There is no database or file storage.
* There is no editing/updating feature for existing loot.
* There is no persistence or backup system.
* The project is a small CLI practice application rather than a production application.
