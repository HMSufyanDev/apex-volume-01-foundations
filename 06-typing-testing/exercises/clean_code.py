def process(data):
    x = data["budget"]
    y = x * 0.10
    z = x - y

    # calculate result
    print(z)

    return z

# 1. `process` is unclear.
# 2. `data` is vague.
# 3. `x`, `y`, `z` are unclear.
# 4. `0.10` is a magic number.
# 5. The comment doesn't add useful information.
# 6. The function has no docstring.
# 7. The code doesn't clearly communicate what it's calculating.


def calculate_remaining_budget(financial_records: dict[str, float]) -> float:
    """
    Calculate the remaining budget after deducting a 10% standard tax.

    """
    TAX_RATE = 0.10

    initial_budget = financial_records["budget"]
    tax_amount = initial_budget * TAX_RATE
    remaining_budget = initial_budget - tax_amount

    return remaining_budget