# revenue: float = 5000
# expenses: float = 1000
# platform_fee: float = 0.10

# fee_amount: float = revenue * platform_fee
# net_income: float = revenue - expenses - fee_amount

# print(net_income)

'''
It works.
But what if you need to calculate income for 10 different freelancers?
You'd have to repeat the same logic again and again.
That's where a function comes in.
'''

def calculate_net_income(
    revenue: float,
    expenses: float,
    platform_fee: float = 0.10,
) -> float:
    fee_amount = revenue * platform_fee
    return revenue - expenses - fee_amount

# Now you can reuse it

income_1 = calculate_net_income(5000, 1000)
income_2 = calculate_net_income(10000, 2500)
income_3 = calculate_net_income(7500, 1200)

print(income_1)
print(income_2)
print(income_3)

# Parameters
def greet(name):
    print(f"Hello, {name}!")

greet("Sufyan") # Hello, Sufyan!


# Multiple parameters
def calculate_total(price, quantity):
    return price * quantity

total = calculate_total(500, 3)

print(total) # 1500


# Type hints
def calculate_total(price: float, quantity: int) -> float:
    return price * quantity

'''
price       → float
quantity    → int
return      → float
'''

'''
-> float means:
"This function is expected to return a float."
'''

# Return values
def calculate_total(price: float, quantity: int) -> float:
    return price * quantity

total = calculate_total(500, 3)

print(total) # 1500

# Now the value can be reused.
total = calculate_total(500, 3)
invoice_total = total + 200

# Default parameters
'''
def calculate_net_income(
    revenue: float,
    expenses: float,
    platform_fee: float = 0.10,
) -> float:
'''
# platform_fee: float = 0.10 # is a default parameter 

# income = calculate_net_income(5000, 1000) # so this work

# But we can override it
# income = calculate_net_income(5000, 1000, 0.05)


# Local scope
def calculate_total(price: float, quantity: int) -> float:
    total = price * quantity
    return total

# The variable: total exists inside the function. That's called a local variable.

print(total) # This causes an error because total doesn't exist outside the function.

# Global scope
platform_name: str = "Upwork"
def show_platform():
    print(platform_name)

show_platform()

# The function can read the global variable.
# Output: Upwork

