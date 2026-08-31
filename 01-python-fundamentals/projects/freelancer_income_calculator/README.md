# Freelancer Income Calculator

A simple command-line Python program that calculates a freelancer's monthly income after platform fees and expenses.

I built this as one of my first Project APEX projects to practice combining user input, calculations, conditions, loops, and basic validation.

## What It Does

The program asks for:

* Number of clients
* Average project value
* Platform fee percentage
* Monthly expenses
* USD → PKR exchange rate

It then calculates:

* Gross income
* Platform fees
* Net income in USD
* Net income in PKR
* Whether the $5,000 income target was reached

## Example

```text
How many clients do you have?: 4
What is your average project value?: 1500
What percentage does the platform charge?: 10
What are your monthly expenses?: 500
What is the USD -> PKR exchange rate?: 280

===================== Freelancer Income ====================
Gross income:          $6000
Platform fees:         $600.00
Monthly expenses:      $500
Net income (USD):      $4900.00
Net income (PKR):      PKR 1372000.00
Target ($5,000):       Target not reached!
============================================================
```

## Concepts Practiced

* Variables
* Type hints
* `input()`
* `int()`
* `float()`
* Arithmetic operators
* `if`
* `while`
* Comparison operators
* Basic input validation
* f-strings
* Number formatting

## Validation

The program doesn't allow negative values for:

* Number of clients
* Project value
* Platform fees
* Monthly expenses

The exchange rate must also be greater than zero.

For example:

```text
Error: Number of clients cannot be negative. Try again.
```

The program keeps asking until a valid value is entered.

## How It Works

The main calculations are:

```text
Gross Income
= Number of Clients × Average Project Value

Platform Fee
= Gross Income × (Platform Fee % / 100)

Net Income
= Gross Income - Platform Fee - Monthly Expenses

PKR Income
= Net Income × Exchange Rate
```

## How to Run

Make sure Python is installed, then run:

```bash
python freelancer_income_calculator.py
```

## What I Learned

This project was useful because it was the first time I combined several Python concepts into one small real-world program.

Instead of just practicing individual syntax, I had to think about the actual flow of the program:

```text
Input
 ↓
Validation
 ↓
Calculation
 ↓
Condition
 ↓
Output
```
