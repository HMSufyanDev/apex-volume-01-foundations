def format_report(
    project_name: str,
    client_budget: float,
    estimated_hours: int,
    platform_fee_percent: float,
    other_expenses: float,
    platform_fee_amount: float,
    total_costs: float,
    net_profit: float,
    hourly_rate: float,
    profit_margin: float,
    verdict: str,
    report_id: str,
    current_date: str
) -> str:
    
    # Display platform percentage properly
    platform_pct_str = f"{int(platform_fee_percent * 100) if (platform_fee_percent * 100).is_integer() else platform_fee_percent * 100}%"

    report = f"""
==================================================
         FREELANCE PROJECT PROFIT ANALYZER
==================================================

Report ID: {report_id}
Date: {current_date}

PROJECT DETAILS
--------------------------------------------------

Project: {project_name}

Client Budget:        ${client_budget:,.2f}
Estimated Hours:      {estimated_hours} hours
Platform Fee:         {platform_pct_str}
Other Expenses:       ${other_expenses:,.2f}

FINANCIAL BREAKDOWN
--------------------------------------------------

Gross Revenue:        ${client_budget:,.2f}
Platform Fee:         -${platform_fee_amount:,.2f}
Other Expenses:       -${other_expenses:,.2f}

Total Costs:          -${total_costs:,.2f}

NET PROFIT:           ${net_profit:,.2f}

PERFORMANCE ANALYSIS
--------------------------------------------------

Effective Hourly Rate: ${hourly_rate:,.2f}/hour
Profit Margin:         {profit_margin:.2f}%

PROJECT VERDICT:
{verdict.upper()} PROJECT

==================================================
"""
    return report