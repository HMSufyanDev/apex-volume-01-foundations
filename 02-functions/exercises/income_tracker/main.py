import calculations, formatting, get_info

# Get information from uesr
client_count = get_info.get_client_count()
project_price = get_info.get_project_price()
software_cost = get_info.get_software_cost()
internet_cost = get_info.get_internet_cost()
other_expenses = get_info.get_other_expenses()
platform_fee = get_info.get_platform_fee()
exchange_rate = get_info.get_exchange_rate()


# Calculation
revenue = calculations.calculate_revenue(client_count, project_price)
total_expenses = calculations.calculate_total_expenses(software_cost, internet_cost, other_expenses)
net_income = calculations.calculate_net_income(revenue, total_expenses, platform_fee)
net_income_pkr = calculations.calculate_net_icome_pkr(net_income, exchange_rate)
target = calculations.calculate_target(net_income)
 

# Formatting
format_revenue = formatting.format_currency_usd(revenue)
format_expenses = formatting.format_currency_usd(total_expenses)
format_net_income_usd = formatting.format_currency_usd(net_income)
format_net_income_pkr = formatting.format_currency_pkr(net_income_pkr)

# --- Output ---
print()
print("===================== Freelancer Income ====================")
print(f"Revenue:               {format_revenue}")
print(f"Monthly expenses:      {format_expenses}")
print(f"Net income (USD):      {format_net_income_usd}")
print(f"Net income (PKR):      {format_net_income_pkr}")
print(f"Target ($5,000):       {target}")
print("============================================================")