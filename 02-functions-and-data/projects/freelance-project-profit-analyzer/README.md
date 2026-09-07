# Freelance Project Profit Analyzer

A command-line Python application that analyzes the profitability of a freelance project.

This project helps freelancers look beyond the client budget and calculate the actual financial value of a project.

It was built as part of **Project APEX — Week 2: Functions and Modular Thinking**.

---

# Project Idea

When freelancers receive a project offer, they often focus only on the client budget.

For example:

```text
Client Budget: $1,000
```

But the actual profitability of a project can be different after considering:

* Platform fees
* Other expenses
* Time required to complete the project

This application calculates the financial profitability of a freelance project.

The main idea is:

```text
Revenue ≠ Profit
```

---

# Features

The program asks for:

* Project name
* Client budget
* Estimated working hours
* Platform fee percentage
* Other expenses

The program then calculates:

* Gross revenue
* Platform fee amount
* Total costs
* Net profit
* Effective hourly rate
* Profit margin

Finally, it provides a project profitability verdict based on the effective hourly rate.

The application also generates:

* A unique report ID
* The current date
* A structured financial report

---

# How It Works

```text
START
  ↓
Get project information
  ↓
Validate user input
  ↓
Calculate platform fee
  ↓
Calculate total costs
  ↓
Calculate net profit
  ↓
Calculate effective hourly rate
  ↓
Calculate profit margin
  ↓
Analyze project profitability
  ↓
Generate report ID
  ↓
Get current date
  ↓
Format and display financial report
  ↓
END
```

---

# Input Validation

The application validates user input before performing calculations.

## Project Name

The project name:

* Cannot be empty

## Client Budget

The client budget:

* Cannot be empty
* Cannot contain spaces
* Must be a valid number
* Cannot be negative

## Estimated Hours

The estimated working hours:

* Cannot be empty
* Cannot contain spaces
* Must be a valid integer
* Must be greater than 0

## Platform Fee Percentage

The platform fee percentage:

* Cannot be empty
* Cannot contain spaces
* Must be a valid number
* Must be between 0 and 100

The entered percentage is converted internally into decimal form.

Example:

```text
10
```

Internally:

```text
0.10
```

## Other Expenses

Other expenses:

* Cannot be empty
* Cannot contain spaces
* Must be a valid number
* Cannot be negative

---

# Calculations

## Gross Revenue

The gross revenue is the total budget provided by the client.

```text
Gross Revenue = Client Budget
```

---

## Platform Fee

The platform fee is calculated using:

```text
Platform Fee Amount =
Gross Revenue × Platform Fee Percentage
```

Example:

```text
$1,500 × 10%

= $150
```

---

## Total Costs

```text
Total Costs =
Platform Fee + Other Expenses
```

Example:

```text
$150 + $200

= $350
```

---

## Net Profit

```text
Net Profit =
Gross Revenue - Total Costs
```

Example:

```text
$1,500 - $350

= $1,150
```

---

## Effective Hourly Rate

This calculation helps determine how much the freelancer is actually earning per hour after costs.

```text
Effective Hourly Rate =
Net Profit ÷ Estimated Hours
```

Example:

```text
$1,150 ÷ 40 hours

= $28.75/hour
```

If the estimated hours are less than or equal to zero, the calculation function returns:

```text
0.0
```

However, the input validation system prevents the user from entering zero or negative hours.

---

## Profit Margin

```text
Profit Margin =
(Net Profit ÷ Gross Revenue) × 100
```

Example:

```text
($1,150 ÷ $1,500) × 100

= 76.67%
```

If the gross revenue is less than or equal to zero, the calculation function returns:

```text
0.0
```

---

# Project Verdict

The program analyzes the effective hourly rate and provides a profitability verdict.

| Effective Hourly Rate | Verdict         |
| --------------------- | --------------- |
| $50 or above          | Excellent       |
| $30–$49.99            | Good            |
| $15–$29.99            | Acceptable      |
| $5–$14.99             | Low Profit      |
| Below $5              | Not Recommended |

The final report displays the verdict followed by the word `PROJECT`.

For example:

```text
ACCEPTABLE PROJECT
```

This helps transform raw financial calculations into a simple project evaluation.

---

# Example Output

```text
==================================================
         FREELANCE PROJECT PROFIT ANALYZER
==================================================

Report ID: PRJ-7824
Date: September 07, 2026

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

---

# Project Structure

```text
freelance-project-profit-analyzer/
│
├── main.py
├── calculations.py
├── validators.py
├── generators.py
├── formatting.py
└── README.md
```

---

# File Responsibilities

## `main.py`

The main entry point of the application.

Responsible for:

* Collecting validated project information
* Calling calculation functions
* Analyzing project profitability
* Generating report metadata
* Calling the report formatting function
* Displaying the final report

The application runs through:

```python
if __name__ == "__main__":
    main()
```

This ensures that the main application runs when `main.py` is executed directly.

---

## `validators.py`

Handles user input validation.

### Functions

```python
get_project_name()
get_non_negative_float()
get_positive_int()
get_valid_percentage()
```

### Responsibilities

The validation system handles:

* Empty input
* Spaces in numerical input
* Invalid numerical values
* Negative financial values
* Zero or negative working hours
* Invalid platform percentages

The module uses:

```python
try
except ValueError
```

to safely handle invalid numerical input.

---

## `calculations.py`

Contains all financial calculation and project analysis functions.

### Functions

```python
calculate_platform_fee()
calculate_total_costs()
calculate_net_profit()
calculate_hourly_rate()
calculate_profit_margin()
analyze_project()
```

This module is responsible for:

* Calculating the platform fee
* Calculating total project costs
* Calculating net profit
* Calculating the effective hourly rate
* Calculating the profit margin
* Determining the project profitability verdict

The functions focus on processing data and returning values instead of printing results directly.

---

## `generators.py`

Responsible for generating report metadata.

### Functions

```python
generate_report_id()
get_current_date()
```

The module uses Python's standard library:

* `random`
* `datetime`

The report ID is generated in this format:

```text
PRJ-1234
```

The current date is formatted like:

```text
September 07, 2026
```

---

## `formatting.py`

Responsible for formatting the complete financial report.

### Function

```python
format_report()
```

This function receives all project data, calculations, metadata, and the final verdict, then returns a formatted string for display.

The report includes:

* Project details
* Financial breakdown
* Performance analysis
* Project verdict
* Report ID
* Current date

This keeps formatting and presentation logic separate from calculations and validation logic.

---

# Application Architecture

Instead of placing all application logic inside one Python file, the project separates responsibilities into different modules.

```text
User Input
    ↓
Validation
    ↓
Financial Calculations
    ↓
Project Analysis
    ↓
Metadata Generation
    ↓
Report Formatting
    ↓
Final Output
```

The `main.py` file connects all these modules together.

This modular structure makes the application easier to:

* Read
* Understand
* Maintain
* Debug
* Expand in the future

---

# Concepts Practiced

This project helped me practice:

* Functions
* Parameters
* Arguments
* Return values
* Type hints
* Default function behavior
* Function design
* One function, one responsibility
* Modules
* Imports
* `if __name__ == "__main__"`
* Input validation
* `try`
* `except ValueError`
* Loops
* Conditional logic
* Financial calculations
* Business logic
* `datetime`
* `random`
* String formatting
* f-strings
* Separation of responsibilities
* Command-line application structure

---

# Key Learning

The most important lesson from this project was understanding the difference between a simple calculation script and a structured application.

Instead of placing everything inside one file:

```text
Input
Calculations
Validation
Analysis
Formatting
Output
```

The program was separated into different modules:

```text
Validation
    ↓
Calculations
    ↓
Project Analysis
    ↓
Metadata Generation
    ↓
Formatting
    ↓
Main Application Flow
```

Each module has a specific responsibility.

This made the application easier to read, understand, maintain, and expand.

It also helped me practice organizing a Python application using modular programming and separation of responsibilities.

---

# Future Improvements

Possible future improvements:

* Add taxes
* Add payment processing fees
* Add multiple expense categories
* Compare multiple projects
* Save project reports to files
* Add monthly profit analysis
* Add project history
* Export reports to CSV or PDF
* Build a graphical interface
* Create a web application version

---

# Built With

* Python
* Python Standard Library
* VS Code

---

# Project APEX

This project is part of my **Project APEX** journey.

The goal of Project APEX is to build strong software engineering fundamentals through consistent learning and project building, with the long-term goal of becoming an AI Software Engineer.
