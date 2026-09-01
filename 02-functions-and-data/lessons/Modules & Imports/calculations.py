# def calculate_revenue(
#     client_count: int,
#     project_price: float,
# ) -> float:
#     return client_count * project_price

# Multiple functions

# def calculate_revenue(
#     client_count: int,
#     project_price: float,
# ) -> float:
#     return client_count * project_price


def calculate_total_expenses(
    software_cost: float,
    internet_cost: float,
    other_expenses: float,
) -> float:
    return software_cost + internet_cost + other_expenses


def calculate_net_income(
    revenue: float,
    expenses: float,
    platform_fee: float = 0.10,
) -> float:
    fee_amount = revenue * platform_fee
    return revenue - expenses - fee_amount


# What is __name__?

def calculate_revenue(
    client_count: int,
    project_price: float,
) -> float:
    return client_count * project_price


if __name__ == "__main__":
    print(calculate_revenue(5, 500))

# If I run: python calculations.py, I get 2500

'''
But if main.py imports:

from calculations import calculate_revenue

the test code inside:

if __name__ == "__main__":

doesn't execute.

Only the function gets imported.
'''
