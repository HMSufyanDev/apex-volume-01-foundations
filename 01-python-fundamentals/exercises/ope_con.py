# Exercise 1 — Grade calculator
score: int = 85

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")


# Exercise 2 — Login eligibility checker
username: str = "sufyan"
password_correct: bool = True

if username and password_correct:
    print("Login successful")
else:
    print("Login failed")


# Exercise 3 — Website quotation calculator
pages: int = 5
price_per_page: int = 100
base_price: int = pages * price_per_page
premium_quotation: str = "Includes a full-scale custom site/E-commerce store with payment gateway integration, advanced speed/security, and 1-month dedicated support."
standard_quotation: str = "Includes up to 3 custom pages, basic SEO, WhatsApp integration, fast loading optimization, and CMS client training."

if base_price >= 500:
    print(f"{premium_quotation}")
else:
    print(f"{standard_quotation}")

# Exercise 4 — Age restriction checker
age: int = 17
if age >= 18:
    print("Allowed")
else:
    print("Not allowed")


# Exercise 5 — Discount calculator
price: float = 1200.0

# 1. Determine discount rate dynamically based on price
if price >= 1000:
    discount_percent = 20
elif price >= 500:
    discount_percent = 10
else:
    discount_percent = 0

# 2. Calculate and display if a discount applies
if discount_percent > 0:
    discount_amount = price * (discount_percent / 100)
    final_price = price - discount_amount
    print(f"Discount applied ({discount_percent}%): ${discount_amount:.2f}")
    print(f"Your final price is: ${final_price:.2f}")
else:
    print("No discount applied.")