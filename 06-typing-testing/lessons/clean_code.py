# Clear Naming
# x = p * 0.1
# what is x? p? 0.1?
# Instead
# platform_fee = project_price * PLATFORM_FEE_RATE

# Functions
# def process(data): Bad
# def save_crm_data(data): Better

# Classes
# class Data: Bad
# class Lead Better
# Even filenames should explain their purpose.

# Don't make names unnecessarily short
# invoice.status is better than i.status

# But don't make names ridiculously long

# Small Functions
# def delete_lead():
    # find lead
    # ask confirmation
    # create backup
    # delete lead
    # save CRM
    # print messages
# This function is doing many jobs.


# Constants
# platform_fee = project_price * 0.10
# What's 0.10? This is called a magic number: A number sitting inside code whose meaning isn't obvious.
# Instead
# PLATFORM_FEE_RATE = 0.10
# platform_fee = project_price * PLATFORM_FEE_RATE
# Why uppercase?
# Python convention uses uppercase for constants:

# Docstrings
# A docstring belongs directly inside a function/class/module.
def calculate_net_income(
    income: float,
    expenses: float
) -> float:
    """Calculate net income after expenses."""
    return income - expenses

# Comment
# Usually explains something inside the code

# Docstring
# Describes what a function/class/module does.