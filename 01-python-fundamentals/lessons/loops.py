# The for loop

for number in range(5):
    print(number)
# output:
# 0
# 1
# 2
# 3
# 4

# range(start, stop, step)
for number in range(0, 11, 2):
    print(number)

# Output:
# 0
# 2
# 4
# 6
# 8
# 10

# Counting backwards
for number in range(5, 0, -1):
    print(number)

# Output:
# 5
# 4
# 3
# 2
# 1

# for loops over lists
names: list[str] = ["James", "Ali", "Ahmed", "John"]
for name in names:
    print(name)

# Output:
# James
# Ali
# Ahmed
# John


# while loops
count: int = 1

while count <= 5:
    print(count)
    count += 1

# Output:
# 1
# 2
# 3
# 4
# 5

# break
for number in range(1, 11):
    if number == 5:
        break

    print(number)

# Output:
# 1
# 2
# 3
# 4

# continue
for number in range(1, 6):
    if number == 3:
        continue

    print(number)

# Output:
# 1
# 2
# 4
# 5

# Nested loops
for row in range(3):
    for column in range(3):
        print(row, column)

# This produces combinations of rows and columns.

# Conceptually:

# row 0:
#     column 0
#     column 1
#     column 2

# row 1:
#     column 0
#     column 1
#     column 2

# row 2:
#     column 0
#     column 1
#     column 2