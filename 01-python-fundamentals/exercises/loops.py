# Calculate the total using a loop.
prices: list[int] = [100, 250, 75, 300, 125]
total: int = 0
for price in prices:
    total += price
print(total)

print(sum(prices)) # same work

# Build a multiplication table.
number: int = int(input("Enter a number: "))

for i in range(1, 11):
    print(f"{number} X {i} = {number * i}")

# Build the password checker.
password: str = "sufyan"
enter_password = None

while enter_password != password:
    enter_password = input("Enter your password: ")
    print("Try Again!")
else:
    print("Login successful!")

