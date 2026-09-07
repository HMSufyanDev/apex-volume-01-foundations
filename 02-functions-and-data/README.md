# Project APEX — Week 2

## Functions and Modular Thinking

Week 2 of Project APEX was focused on learning how to write more organized, reusable, and maintainable Python code.

In Week 1, I focused on the fundamentals of Python such as variables, data types, strings, conditions, loops, and basic program logic.

This week, I moved one step further.

Instead of only thinking about **how to make a program work**, I started learning how to structure the code properly using functions, modules, reusable logic, standard-library tools, and input validation.

I also built two complete command-line projects to apply what I learned.

---

# What I Learned

## Day 1 — Functions

I started the week by learning the fundamentals of functions in Python.

Topics covered:

* Function definition
* Parameters
* Arguments
* Return values
* Local scope
* Global scope
* Default parameters

I learned that functions allow me to take a piece of logic and turn it into something reusable.

For example:

```python
def calculate_net_income(
    revenue: float,
    expenses: float,
    platform_fee: float = 0.10,
) -> float:
    fee_amount = revenue * platform_fee
    return revenue - expenses - fee_amount
```

One of the most important things I learned was the difference between **printing** a result and **returning** a result.

A function that returns a value is usually more reusable because the returned value can be used somewhere else in the program.

For example:

```python
net_income = calculate_net_income(2000, 500)
```

The function calculates the value and gives it back to the program instead of deciding how that value should be displayed.

---

# Day 2 — Function Design + Modules and Imports

On Day 2, I moved beyond simply creating functions and started learning how to design them properly.

## Function Design

Topics covered:

* One function, one responsibility
* Meaningful function names
* Small functions
* Avoiding repeated code
* Inputs and outputs
* Pure functions

I learned that a function should ideally have a clear purpose.

Instead of creating one large function that does everything:

```python
def do_everything():
    ...
```

I learned to break the program into smaller responsibilities:

```python
def get_client_count() -> int:
    ...


def calculate_revenue(
    client_count: int,
    project_price: float,
) -> float:
    ...


def display_summary(
    net_income: float,
) -> None:
    ...
```

This made me start thinking about functions as individual building blocks of an application.

## Modules and Imports

I also learned how to organize Python code across multiple files.

Topics covered:

* Creating multiple Python files
* `import`
* `from x import y`
* `__name__`
* `if __name__ == "__main__"`

For example:

```text
project/
├── main.py
├── calculations.py
├── validators.py
└── formatting.py
```

I learned that I don't need to keep an entire application inside one Python file.

Different parts of the program can be separated into modules based on their responsibilities and then imported when needed.

I also learned the common Python entry-point pattern:

```python
def main() -> None:
    ...


if __name__ == "__main__":
    main()
```

This was an important step toward writing more structured applications.

---

# Day 3 — Useful Python Standard-Library Modules

On Day 3, I explored several useful modules that are already included with Python.

The goal was not to memorize every function inside these modules.

Instead, I wanted to understand **what each module is useful for and when I might need it**.

## `datetime`

Used for working with dates and times.

Example:

```python
from datetime import datetime

current_date = datetime.now()
```

I used this concept in my projects to add the current date to generated reports.

---

## `math`

Used for mathematical operations.

Example:

```python
import math

result = math.sqrt(25)
```

---

## `random`

Used for generating random values.

Example:

```python
import random

number = random.randint(1000, 9999)
```

I used this concept to generate IDs for my project reports.

---

## `statistics`

Used for working with statistical calculations.

Example:

```python
import statistics

average = statistics.mean(data)
```

This is useful when working with collections of numerical data.

---

## `pathlib`

Used for working with files and directories.

Example:

```python
from pathlib import Path

current_directory = Path.cwd()
```

---

# Day 4 — Input Validation

On Day 4, I learned how to make programs safer by handling invalid user input.

Previously, a program could crash if a user entered something that Python could not convert into the expected data type.

For example:

```text
Enter amount: hello
```

If the program expected a number, this could cause an error.

I learned to handle these situations using:

* `try`
* `except`
* `ValueError`
* `while True`
* `continue`
* Type validation
* Business-rule validation

For example:

```python
def get_positive_float(prompt: str) -> float:
    while True:
        raw_value = input(prompt)

        try:
            value = float(raw_value)
        except ValueError:
            print("Please enter a valid number.")
            continue

        if value < 0:
            print("The value cannot be negative.")
            continue

        return value
```

The important idea I learned was that user input should not automatically be trusted.

The program should validate the input before using it.

The general flow became:

```text
User Input
    ↓
Try to convert the value
    ↓
Handle conversion errors
    ↓
Check program rules
    ↓
Accept valid input
```

This became especially useful in both projects I built during the second half of the week.

---

# Day 5 — Project 1

## 🔐 Password Security Analyzer

For the first project, I wanted to build something different from the calculators and simple business programs I had already created.

I built a command-line **Password Security Analyzer**.

The application analyzes a password based on several security requirements and produces a security report.

### Features

The program checks:

* Password length
* Uppercase letters
* Lowercase letters
* Numbers
* Special characters
* Security score
* Password strength
* Security recommendations

It also generates:

* Analysis ID
* Current date
* Professional command-line report

### Example Flow

```text
Enter Password
      ↓
Validate Input
      ↓
Analyze Password
      ↓
Calculate Security Score
      ↓
Determine Strength
      ↓
Generate Recommendations
      ↓
Generate Analysis ID
      ↓
Display Report
```

### Example Output

```text
==================================================
           PASSWORD SECURITY ANALYZER
==================================================

Analysis ID: SEC-4821
Date: September 7, 2026

PASSWORD ANALYSIS
--------------------------------------------------

Password Length: 9 characters

SECURITY CHECKS

✓ Contains uppercase letters
✓ Contains lowercase letters
✓ Contains numbers
✓ Contains special characters

--------------------------------------------------

SECURITY SCORE: 80/100

PASSWORD STRENGTH: STRONG

--------------------------------------------------

RECOMMENDATIONS

• Consider increasing the password length to 12+ characters.

==================================================
```

### Concepts Practiced

This project helped me apply:

* Functions
* Parameters
* Return values
* Pure functions
* Boolean logic
* String analysis
* Modules
* Imports
* Input validation
* `random`
* `datetime`
* Separation of responsibilities

More details about this project are available in its own README.

---

# Day 6 — Project 2

## 💼 Freelance Project Profit Analyzer

For the second project, I built a command-line application based around something directly related to freelancing.

The purpose of the application is to help analyze whether a freelance project is actually profitable.

Instead of looking only at the client's budget, the program considers fees, expenses, and estimated working hours.

The main idea is:

```text
Revenue ≠ Profit
```

### Features

The program asks for:

* Project name
* Client budget
* Estimated hours
* Platform fee percentage
* Other expenses

It then calculates:

* Gross revenue
* Platform fee
* Total costs
* Net profit
* Effective hourly rate
* Profit margin
* Project verdict

It also generates:

* Report ID
* Current date
* Professional financial report

### Example Flow

```text
Project Information
        ↓
Input Validation
        ↓
Platform Fee Calculation
        ↓
Total Cost Calculation
        ↓
Net Profit Calculation
        ↓
Hourly Rate Calculation
        ↓
Profit Margin Calculation
        ↓
Project Analysis
        ↓
Generate Report
```

### Example Output

```text
==================================================
          FREELANCE PROJECT PROFIT ANALYZER
==================================================

Report ID: PRJ-7824
Date: September 7, 2026

PROJECT DETAILS
--------------------------------------------------

Project: E-Commerce Website Development

Client Budget:        $1,500.00
Estimated Hours:      40 hours
Platform Fee:         10%
Other Expenses:       $200.00

FINANCIAL BREAKDOWN
--------------------------------------------------

Gross Revenue:        $1,500.00
Platform Fee:         -$150.00
Other Expenses:       -$200.00

Total Costs:          -$350.00

NET PROFIT:           $1,150.00

PERFORMANCE ANALYSIS
--------------------------------------------------

Effective Hourly Rate: $28.75/hour
Profit Margin:         76.67%

PROJECT VERDICT:
ACCEPTABLE PROJECT

==================================================
```

### Concepts Practiced

This project allowed me to combine almost everything I learned during Week 2:

* Functions
* Function design
* Parameters and return values
* Modules
* Imports
* Input validation
* `try` / `except`
* Conditional logic
* Financial calculations
* Business logic
* `datetime`
* `random`
* Separation of responsibilities
* Command-line application structure

More details about this project are available in its own README.

---

# Week 2 Project Structure

```text
week-02-functions-and-modular-thinking/
│
├── README.md
│
├── password-security-analyzer/
│   ├── README.md
│   ├── main.py
│   ├── analyzer.py
│   ├── scoring.py
│   ├── generators.py
│   ├── validators.py
│   └── formatting.py
│
└── freelance-project-profit-analyzer/
    ├── README.md
    ├── main.py
    ├── calculations.py
    ├── generators.py
    ├── validators.py
    └── formatting.py
```

---

# Main Lessons From Week 2

The biggest change for me this week was starting to think about **code organization**, not just code execution.

I learned that a program can work and still be poorly structured.

A better approach is to break an application into smaller pieces where each function and module has a clear responsibility.

My progression this week was:

```text
Basic Python Logic
        ↓
Functions
        ↓
Better Function Design
        ↓
Modules and Imports
        ↓
Standard Library
        ↓
Input Validation
        ↓
Complete Modular Applications
```

I also learned that functions should generally focus on doing their job and returning useful values, while other parts of the program can decide how those values should be displayed or used.

---

# Tools and Technologies

* Python
* Python Standard Library
* VS Code
* Git
* GitHub

---

# Project APEX Progress

Week 2 is another step in my **Project APEX** journey.

The focus this week was not on learning a huge number of new Python features.

Instead, I focused on learning how to take the Python fundamentals from Week 1 and start using them to build programs that are more organized, reusable, and maintainable.

The goal is to continue strengthening these fundamentals before moving into more advanced software engineering concepts.
