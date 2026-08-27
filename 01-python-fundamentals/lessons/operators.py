# Arithmetic operators
print(10 + 5)
print(10 - 5)
print(10 * 5)
print(10 / 5)
print(10 // 3) # floor division # 3
print(10 % 3) # 1
print(2 ** 3) # 8

# Comparison operators
# Operator	Meaning
# ==	    Equal to
# !=	    Not equal to
# >	        Greater than
# <	        Less than
# >=	    Greater than or equal to
# <=	    Less than or equal to

age: int = 22
print(age == 18)
print(age != 18)
print(age > 18)
print(age < 18)
print(age >= 18)
print(age <= 18)

# Assignment Operators
# 1. Basic Assignment (=)
x = 10
print(f"Initial x: {x}")

# 2. Add and Assign (+=) -> Same as: x = x + 5
x += 5
print(f"After x += 5: {x}")  # 15

# 3. Subtract and Assign (-=) -> Same as: x = x - 3
x -= 3
print(f"After x -= 3: {x}")  # 12

# 4. Multiply and Assign (*=) -> Same as: x = x * 2
x *= 2
print(f"After x *= 2: {x}")  # 24

# 5. Divide and Assign (/=) -> Same as: x = x / 4 (returns float)
x /= 4
print(f"After x /= 4: {x}")  # 6.0

# 6. Floor Divide and Assign (//=) -> Same as: x = x // 4 (integer division)
x //= 4
print(f"After x //= 4: {x}")  # 1.0

# 7. Modulus and Assign (%=) -> Same as: y = y % 3 (remainder)
y = 10
y %= 3
print(f"After y %= 3: {y}")  # 1

# 8. Exponent and Assign (**=) -> Same as: y = y ** 4 (power)
y **= 4
print(f"After y **= 4: {y}")  # 1

# 9. Walrus Operator (:=) -> Assigns value inside an expression (Python 3.8+)
if (n := len("Python")) > 3:
    print(f"Length n is: {n}")  # 6



# Logical Operators
age = 20
has_id = True
is_banned = False

# 1. logical AND (and) -> Returns True ONLY IF BOTH conditions are True
can_enter = (age >= 18) and has_id
print(f"Can enter: {can_enter}")  # True (Both are True)

# 2. logical OR (or) -> Returns True IF AT LEAST ONE condition is True
gets_discount = (age < 12) or (age >= 65)
print(f"Gets discount: {gets_discount}")  # False (Neither is True)

# 3. logical NOT (not) -> Reverses the boolean value (True becomes False, and vice-versa)
is_allowed = not is_banned
print(f"Is allowed: {is_allowed}")  # True (reverses False to True)


# Short-Circuiting Feature:
# 'and' stops checking if the 1st condition is False
# 'or' stops checking if the 1st condition is True
print("\n--- Short-Circuit Example ---")
result = False and print("This will NEVER run")
result_or = True or print("This won't run either")
print("Short-circuiting works as expected!")