# Project APEX — Week 1

## Python Foundations

This was my first week of Project APEX.

The goal of this week was not to learn a huge amount of Python, but to understand the basic building blocks properly and actually use them to build small programs.

I focused on understanding how Python code is written, executed, and how basic programming logic works.

---

## What I Learned

### Day 1 — Environment & Execution

I learned:

* What Python is
* Interpreter vs compiler
* How a `.py` file is executed
* Python REPL
* Running Python through the VS Code terminal
* `print()`
* Comments
* Basic Python syntax
* Indentation
* How to read basic error messages

I also learned the difference between:

```text
Writing code
Saving code
Running code
Seeing program output
```

My first program was:

```python
print("Project APEX started")
```

---

### Day 2 — Variables & Data Types

I learned how to store and work with different types of data.

Topics covered:

* Variables
* Assignment
* Naming conventions
* `str`
* `int`
* `float`
* `bool`
* `None`
* `type()`
* Type conversion
* Basic type hints

Example:

```python
name: str = "Sufyan"

semester: int = 4

target_income_usd: int = 5000
```

I also practiced basic calculations such as:

* Currency conversion
* Age calculation
* Rectangle area
* Temperature conversion

---

### Day 3 — Strings

I learned how to work with text in Python.

Topics covered:

* Creating strings
* Indexing
* Slicing
* `strip()`
* `lower()`
* `upper()`
* `replace()`
* `split()`
* `join()`
* f-strings

I practiced things like:

* Normalizing names
* Extracting information from emails
* Counting words
* Creating invoice messages
* Hiding parts of phone numbers

---

### Day 4 — Operators & Conditions

This was where I started making programs that could actually make decisions.

I learned:

* Arithmetic operators
* Comparison operators
* Logical operators
* `if`
* `elif`
* `else`
* Nested conditions
* Truthy and falsy values

I practiced building:

* Grade calculators
* Login eligibility checkers
* Website quotation logic
* Age restriction checkers
* Discount calculators

---

### Day 5 — Loops

I learned how to repeat operations instead of writing the same code again and again.

Topics covered:

* `for`
* `while`
* `range()`
* Loop variables
* `break`
* `continue`
* Infinite loops

I practiced:

* Printing numbers
* Printing even numbers
* Calculating totals
* Building multiplication tables
* Repeatedly asking for a password

This helped me understand how programs can process multiple pieces of data automatically.

---

### Day 6 — Mini Project

For Day 6, I combined the concepts I learned throughout the week and built my first proper Python mini project.

## Freelancer Income Calculator

A command-line calculator that takes:

* Number of clients
* Average project value
* Monthly expenses
* Platform fee percentage
* USD → PKR exchange rate

It then calculates:

* Gross income
* Platform fees
* Monthly expenses
* Net income in USD
* Net income in PKR
* Whether the $5,000 target was reached

I also added basic validation so negative values are rejected.

This project helped me combine variables, data types, type conversion, arithmetic, conditions, input handling, loops, and basic validation into one working program.

---

## Practice Projects Built During the Week

While practicing the concepts from Days 1–5, I also built a few small programs to reinforce what I was learning.

### 1. Rock, Paper, Scissors

A command-line Rock, Paper, Scissors game where I play against the computer.

The game includes:

* Random computer choices
* User input
* Input validation
* Score tracking
* Draw tracking
* A continuous game loop
* `break` to quit
* `continue` for invalid input
* Final result

This project gave me a practical reason to use loops and conditions together.

---

### 2. Website Pricing Engine

A small pricing system for generating website quotations.

The program calculates the price based on:

* Number of pages
* Price per page
* Whether e-commerce is required

It then applies discounts depending on the total price.

The final output gives the client a quotation with the discount and final price.

This project was especially useful because it connects Python programming with something I could actually use in my freelancing/business context.

---

## Concepts I Used Across the Week

```text
Python execution

Variables

Type hints

Data types

Type conversion

Strings

String methods

Indexing

Slicing

f-strings

Arithmetic

Comparisons

Logical operators

if / elif / else

Truthy / falsy

for loops

while loops

range()

break

continue

input()

Basic validation
```

---

## What I Can Do Now

After Week 1, I can write small Python programs that:

* Take input from a user
* Store and manipulate data
* Perform calculations
* Make decisions
* Repeat operations
* Validate basic input
* Format output
* Combine multiple concepts into one program

The biggest thing I learned this week is that learning syntax isn't enough.

I need to be able to take a simple problem, break it into steps, and turn those steps into code.

---

## Week 1 Status

**Completed**

Next step: continue building on these fundamentals and gradually move toward more structured Python programs.
