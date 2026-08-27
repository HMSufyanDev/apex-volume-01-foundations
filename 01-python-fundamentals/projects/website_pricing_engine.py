
per_page: int = 100

client_name: str = input("Enter Your Name: ")
pages: int = int(input("How many pages you want?: "))
has_ecommerce: bool = input("Do you want ecommerce? Y/N: ").strip().lower() == "y"

base_price = per_page * pages

# Add Extra Charges
extra_charges = 300 if has_ecommerce else 0
total = base_price + extra_charges

# Display calculation breakdown
if has_ecommerce:
    print(f"Base price: ${base_price}, +$300 for e-commerce = ${total}")
else:
    print(f"Base price: ${total}")

# Check Discount Eligibility
if total >= 1000:
    discount_percent = 20
elif total >= 500:
    discount_percent = 10
else:
    discount_percent = 0

# Calculate Final Price
discount_amount = total * (discount_percent / 100)
final_price = total - discount_amount

# Generate Output Message
if discount_percent > 0:
    print(f"Discount applied ({discount_percent}%): -${discount_amount:.2f}")
else:
    print("No discount applied.")

print(f"Hi {client_name}, your final website quotation is: ${final_price:.2f}")