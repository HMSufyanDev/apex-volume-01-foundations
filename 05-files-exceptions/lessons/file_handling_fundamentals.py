# File handling = using Python to interact with files.
# open()

file = open("notes.txt")

# "r" — Read
file = open("notes.txt", "r")
content = file.read()
print(content)
# Note: "r" expects the file to already exist.

# "w" — Write
file = open("notes.txt", "w")
file.write("Hello Python")
file.close()
# Note: "w" replaces existing content.

# "a" — Append
# Add new content to the end of the existing file.
file = open("notes.txt", "a")
file.write("\nLearning files")
file.close()

# "x" — Create
file = open("new_file.txt", "x")
# If new_file.txt doesn't exist: new_file.txt is created 
# But if exist: FileExistsError
# in "w", if file doesnt exist, create it, if exist replace it 

# encoding="utf-8"
open("notes.txt", "r", encoding="utf-8")
# Computers ultimately store text as numbers.
# Characters need to be encoded into bytes.
# UTF-8 is a standard way of representing text.
# It supports a huge range of characters: