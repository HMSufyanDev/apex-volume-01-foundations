# Password Security Analyzer

A command-line Python application that analyzes the strength of a password based on multiple security rules.

This project was built as part of **Project APEX — Week 2: Functions and Modular Thinking**.

The main goal of this project was to practice writing reusable functions, organizing code into multiple modules, separating responsibilities, and building a complete Python application using the concepts learned during Week 2.

---

## Features

The Password Security Analyzer checks a password for:

* Password length
* Uppercase letters
* Lowercase letters
* Numbers
* Special characters
* Overall security score
* Password strength level
* Security recommendations

The application also generates:

* A unique analysis ID
* The current date
* A structured command-line security report

---

## How It Works

The program follows this flow:

```text
START
  ↓
Ask user for password
  ↓
Validate password input
  ↓
Generate analysis ID and current date
  ↓
Analyze password characteristics
  ↓
Calculate security score
  ↓
Determine password strength
  ↓
Generate recommendations
  ↓
Format the security report
  ↓
Display final output
  ↓
END
```

---

## Password Validation

Before analyzing the password, the program validates the user's input.

The password cannot:

* Be empty
* Contain spaces

If the user enters an invalid password, the program displays an error message and asks again.

### Example

```text
Enter Your Password:
Password cannot be empty, try again!
```

Or:

```text
Enter Your Password: hello password
Spaces not allowed!, try again!
```

---

## Security Checks

The program analyzes the following password characteristics:

| Security Check     | Description                                               |
| ------------------ | --------------------------------------------------------- |
| Password Length    | Checks the total number of characters                     |
| Uppercase Letters  | Checks for uppercase characters using `isupper()`         |
| Lowercase Letters  | Checks for lowercase characters using `islower()`         |
| Numbers            | Checks for numeric characters using `isdigit()`           |
| Special Characters | Checks for non-alphanumeric and non-whitespace characters |

### Example Password

```text
Hello123!
```

The program can detect:

```text
✓ Uppercase letters
✓ Lowercase letters
✓ Numbers
✓ Special characters
```

---

## Security Score System

The password receives a security score out of **100 points**.

The scoring system works as follows:

| Requirement                               | Points |
| ----------------------------------------- | -----: |
| Password length is at least 8 characters  |    +20 |
| Password length is at least 12 characters |    +10 |
| Password length is at least 16 characters |    +10 |
| Contains uppercase letters                |    +15 |
| Contains lowercase letters                |    +15 |
| Contains numbers                          |    +15 |
| Contains special characters               |    +15 |

Maximum possible score:

```text
100/100
```

---

## Password Strength Levels

The security score is converted into a password strength level.

| Score  | Strength  |
| ------ | --------- |
| 0–39   | Very Weak |
| 40–59  | Weak      |
| 60–74  | Moderate  |
| 75–89  | Strong    |
| 90–100 | Excellent |

---

## Recommendations System

The program generates recommendations based on the password's weaknesses.

Possible recommendations include:

* Increase password length to at least 8 characters
* Increase password length to 12+ characters
* Increase password length to 16+ characters
* Add at least one uppercase letter
* Add at least one lowercase letter
* Add at least one number
* Add at least one special character

If the password meets all the basic security criteria, the program displays:

```text
Great job! Your password meets all basic security criteria.
```

---

## Example Output

```text
==================================================
            PASSWORD SECURITY ANALYZER
==================================================

Analysis ID: SEC-4821
Date: September 07, 2026

PASSWORD ANALYSIS
--------------------------------------------------

Password Length: 9 characters

SECURITY CHECKS

✓ Contains uppercase letters
✓ Contains lowercase letters
✓ Contains numbers
✓ Contains special characters
✗ Password should be at least 12 characters

--------------------------------------------------

SECURITY SCORE: 80/100

PASSWORD STRENGTH: STRONG

--------------------------------------------------

RECOMMENDATIONS

• Increase length to 12+ characters for better protection.

==================================================
```

---

## Project Structure

```text
password-security-analyzer/
│
├── main.py
├── validators.py
├── analyzer.py
├── scoring.py
├── generators.py
├── formatting.py
└── README.md
```

---

# File Responsibilities

## `main.py`

The main entry point of the application.

Responsible for:

* Getting validated user input
* Generating the analysis ID
* Getting the current date
* Calling functions from other modules
* Connecting the complete application flow
* Displaying the final formatted report

---

## `validators.py`

Handles password input validation.

### Function

```python
get_valid_password()
```

The program ensures that the user:

* Does not submit an empty password
* Does not include spaces in the password

---

## `analyzer.py`

Contains functions responsible for analyzing password characteristics.

### Functions

```python
has_number()
has_uppercase()
has_lowercase()
has_special_character()
get_password_length()
```

These functions determine whether a password contains the required character types and calculate its length.

---

## `scoring.py`

Contains the logic for calculating password security.

### Functions

```python
calculate_security_score()
get_password_strength()
get_recommendations()
```

This module is responsible for:

* Calculating the security score
* Determining the password strength level
* Generating security recommendations

---

## `generators.py`

Responsible for generating application metadata.

### Functions

```python
generate_analysis_id()
get_current_date()
```

The module uses Python's standard library:

* `random`
* `datetime`

The analysis ID is generated in this format:

```text
SEC-1234
```

---

## `formatting.py`

Responsible for formatting the final command-line report.

### Functions

```python
format_header()
format_password_analysis()
format_security_checks()
format_score_summary()
format_recommendations()
```

This module keeps the presentation logic separate from the business logic of the application.

---

# Application Architecture

Instead of placing all logic inside one Python file, the application separates responsibilities into different modules.

```text
User Input
    ↓
Validation
    ↓
Password Analysis
    ↓
Security Scoring
    ↓
Strength Detection
    ↓
Recommendation Generation
    ↓
Metadata Generation
    ↓
Output Formatting
    ↓
Final Report
```

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
* Boolean values
* Conditional logic
* Loops
* String analysis
* Generator expressions
* Built-in string methods
* `any()`
* Input validation
* Modules
* Imports
* Separation of responsibilities
* Random number generation
* Date and time handling
* Type hints
* Command-line application structure

---

# Key Learning

One of the main goals of this project was to avoid putting all the application logic inside `main.py`.

Instead of building one large Python file, the application was divided into multiple responsibilities:

```text
Input
  ↓
Validation
  ↓
Analysis
  ↓
Scoring
  ↓
Recommendations
  ↓
Generation
  ↓
Formatting
```

Each module has a specific responsibility.

This helped me understand how larger Python applications can be organized into smaller, reusable, and easier-to-maintain components.

---

# Future Improvements

Possible improvements for future versions:

* Check against common or weak passwords
* Detect repeated characters
* Detect repeated patterns
* Add password generation
* Add password entropy calculation
* Analyze multiple passwords
* Save security reports to files
* Add unit tests
* Build a graphical user interface
* Create a web version

---

# Built With

* Python
* Python Standard Library
* VS Code

---

# Project APEX

This project is part of my **Project APEX** journey.

Project APEX is my long-term roadmap for building strong software engineering fundamentals and developing the skills required to become an AI Software Engineer.

My goal is to eventually build real-world AI systems, backend applications, intelligent products, and scalable software.
