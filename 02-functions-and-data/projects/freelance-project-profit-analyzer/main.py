from validators import (
    get_project_name,
    get_non_negative_float,
    get_positive_int,
    get_valid_percentage
)
from generators import generate_report_id, get_current_date
from calculations import (
    calculate_platform_fee,
    calculate_total_costs,
    calculate_net_profit,
    calculate_hourly_rate,
    calculate_profit_margin,
    analyze_project
)
from formatting import format_report


def main():
    print("--- Freelance Project Profit Analyzer ---")
    
    # 1. Collect user inputs using validators
    project_name = get_project_name()
    client_budget = get_non_negative_float("Enter client budget ($): ")
    estimated_hours = get_positive_int("Enter estimated hours: ")
    platform_percentage = get_valid_percentage()
    other_expenses = get_non_negative_float("Enter other expenses ($): ")

    # 2. Perform calculations
    platform_fee = calculate_platform_fee(client_budget, platform_percentage)
    total_costs = calculate_total_costs(platform_fee, other_expenses)
    net_profit = calculate_net_profit(client_budget, total_costs)
    hourly_rate = calculate_hourly_rate(net_profit, estimated_hours)
    profit_margin = calculate_profit_margin(net_profit, client_budget)
    verdict = analyze_project(hourly_rate)

    # 3. Generate metadata
    report_id = generate_report_id()
    current_date = get_current_date()

    # 4. Format and display report
    report_output = format_report(
        project_name=project_name,
        client_budget=client_budget,
        estimated_hours=estimated_hours,
        platform_fee_percent=platform_percentage,
        other_expenses=other_expenses,
        platform_fee_amount=platform_fee,
        total_costs=total_costs,
        net_profit=net_profit,
        hourly_rate=hourly_rate,
        profit_margin=profit_margin,
        verdict=verdict,
        report_id=report_id,
        current_date=current_date
    )

    print(report_output)


if __name__ == "__main__":
    main()