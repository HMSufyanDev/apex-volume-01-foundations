# Number of clients (must be >= 0)
number_of_clients: int = int(input("How many clients do you have?: "))
while number_of_clients < 0:
    print("Error: Number of clients cannot be negative. Try again.")
    number_of_clients = int(input("How many clients do you have?: "))

# Average project value (must be >= 0)
average_project_value: int = int(input("What is your average project value?: "))
while average_project_value < 0:
    print("Error: Project value cannot be negative. Try again.")
    average_project_value = int(input("What is your average project value?: "))

# Platform charge percentage (must be >= 0)
percentage_platform_charge: float = float(input("What percentage does the platform charge?: "))
while percentage_platform_charge < 0:
    print("Error: Platform fee cannot be negative. Try again.")
    percentage_platform_charge = float(input("What percentage does the platform charge?: "))

# Monthly expenses (must be >= 0)
monthly_expenses: int = int(input("What are your monthly expenses?: "))
while monthly_expenses < 0:
    print("Error: Expenses cannot be negative. Try again.")
    monthly_expenses = int(input("What are your monthly expenses?: "))

# Exchange rate (must be > 0)
exchange_rate: float = float(input("What is the USD -> PKR exchange rate?: "))
while exchange_rate <= 0:
    print("Error: Exchange rate must be greater than zero. Try again.")
    exchange_rate = float(input("What is the USD -> PKR exchange rate?: "))


# --- Calculations ---
gross_income: int = number_of_clients * average_project_value
platform_fee: float = gross_income * (percentage_platform_charge / 100)

net_income: float = gross_income - platform_fee - monthly_expenses
income_in_pkr: float = net_income * exchange_rate

reached: str = ""
if net_income >= 5000:
    reached = "Target reached!"
else:
    reached = "Target not reached!"


# --- Output ---
print()
print("===================== Freelancer Income ====================")
print(f"Gross income:          ${gross_income}")
print(f"Platform fees:         ${platform_fee:.2f}")
print(f"Monthly expenses:      ${monthly_expenses}")
print(f"Net income (USD):      ${net_income:.2f}")
print(f"Net income (PKR):      PKR {income_in_pkr:.2f}")
print(f"Target ($5,000):       {reached}")
print("============================================================")