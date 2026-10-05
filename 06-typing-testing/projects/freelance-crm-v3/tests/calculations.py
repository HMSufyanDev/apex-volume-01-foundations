def calculate_net_income(
    revenue: float,
    expenses: float,
    platform_fee: float
) -> float:
    fee = revenue * platform_fee
    return revenue - expenses - fee