def calculate_revenue(
    client_count: int,
    project_price: float,
) -> float:
    return client_count * project_price


def calculate_total_expenses(
    software_cost: float,
    internet_cost: float,
    other_expenses: float,
) -> float:
    return software_cost + internet_cost + other_expenses

def calculate_net_income(
    revenue: float,
    expenses: float,
    platform_fee: float = 10,
) -> float:
    fee_amount = revenue * (platform_fee / 100)
    return revenue - expenses - fee_amount

def calculate_net_icome_pkr(
        net_income: float,
        exchange_rate: float
) -> float:
    net_income_pkr = net_income * exchange_rate
    return net_income_pkr

def calculate_target(
        net_income: float,
) -> str:
    if net_income >= 5000:
        return "Target reached!"
    else:
        return "Target not reached!"