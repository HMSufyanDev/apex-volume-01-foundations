# Greeting Function
def greet_user(name: str) -> str:
    return f"Hi, {name}"

message = greet_user("Sufyan!")
print(message)


# Calculate Profit
def calculate_profit(revenue: float, expenses: float) -> float:
    return revenue - expenses

profit = calculate_profit(5000, 2000)
print(profit)

# Freelancer Income
def calculate_net_income(revenue: float, expenses: float, platform_fee: float = 0.10) -> float:
    platform_fee_amount = revenue * platform_fee
    return revenue - expenses - platform_fee_amount

# Test 1: Default platform fee (10%)
income1 = calculate_net_income(5000, 1000)
print(income1)  # Output: 3500.0

# Test 2: Custom platform fee (5%)
income2 = calculate_net_income(5000, 1000, 0.05)
print(income2)  # Output: 3750.0



# Function combination
def calculate_revenue(
    hourly_rate: float,
    hours: int,
) -> float:
    return hourly_rate * hours

def calculate_net_income(
    revenue: float,
    expenses: float,
    platform_fee: float = 0.10,
) -> float:
    fee_amount = revenue * platform_fee
    return revenue - expenses - fee_amount

revenue = calculate_revenue(25, 100)

income = calculate_net_income(revenue, 500)

print(income)