def calculate_platform_fee(gross_revenue: float, percentage: float) -> float:
    return gross_revenue * percentage


def calculate_total_costs(fee_amount: float, other_expenses: float) -> float:
    return fee_amount + other_expenses


def calculate_net_profit(gross_revenue: float, total_cost: float) -> float:
    return gross_revenue - total_cost


def calculate_hourly_rate(net_profit: float, estimated_hours: float) -> float:
    if estimated_hours <= 0:
        return 0.0
    return net_profit / estimated_hours


def calculate_profit_margin(net_profit: float, gross_revenue: float) -> float:
    if gross_revenue <= 0:
        return 0.0
    return (net_profit / gross_revenue) * 100


def analyze_project(hourly_rate: float) -> str:
    if hourly_rate >= 50:
        return "Excellent"
    elif hourly_rate >= 30:
        return "Good"
    elif hourly_rate >= 15:
        return "Acceptable"
    elif hourly_rate >= 5:
        return "Low Profit"
    else:
        return "Not Recommended"