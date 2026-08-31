# Website Pricing Engine

A small command-line Python program that generates a website quotation based on the client's requirements.

I built this project as part of Project APEX to practice turning simple business pricing rules into working program logic.

## What It Does

The program asks for:

* Client name
* Number of website pages
* Whether the client wants e-commerce

The base website price is calculated using:

```text
$100 × number of pages
```

If e-commerce is selected, an additional `$300` is added.

The program then checks whether the client qualifies for a discount.

## Pricing Rules

### Base Price

```text
$100 per page
```

### E-commerce

```text
+$300
```

### Discounts

```text
Total >= $1,000 → 20% discount

Total >= $500 → 10% discount

Below $500 → No discount
```

## Example

```text
Enter Your Name: James
How many pages you want?: 8
Do you want ecommerce? Y/N: y

Base price: $800, +$300 for e-commerce = $1100
Discount applied (20%): -$220.00
Hi James, your final website quotation is: $880.00
```

## Concepts Practiced

* Variables
* Type hints
* `input()`
* `int()`
* `bool`
* `strip()`
* `lower()`
* Arithmetic operators
* Conditional expressions
* `if / elif / else`
* Comparison operators
* f-strings
* Percentage calculations

## Program Flow

```text
Client information
       ↓
Calculate base price
       ↓
Check e-commerce
       ↓
Add extra charge if needed
       ↓
Calculate total
       ↓
Check discount eligibility
       ↓
Calculate discount
       ↓
Calculate final price
       ↓
Generate quotation
```

## Why I Built It

I wanted one of my first projects to connect programming with something practical.

Website pricing is something I can actually use in my freelancing work, so this project helped me understand how business rules can be converted into program logic.

For example:

```text
"If the client wants e-commerce, add $300."

"If the total is at least $1,000, give a 20% discount."
```

These simple business rules become actual Python conditions.

## How to Run

Run the Python file from the terminal:

```bash
python website_pricing_engine.py
```

Then enter the requested information.

## What I Learned

The main lesson from this project was that programming isn't just about syntax.

It's about taking rules like:

```text
If this happens → do this
Otherwise → do something else
```

and translating them into code that a computer can execute.
