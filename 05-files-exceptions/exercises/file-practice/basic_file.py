file = open("notes.txt", "w", encoding="utf-8")
file.write("Hello, I am learning Python file handling.")
file.close()

with open("notes.txt", "r") as file:
    content = file.read()

print(content)

with open("notes.txt", "a") as file:
    file.write("\nI am building Project APEX.")


with open("notes.txt", "r") as file:
    content = file.read()

print(content)