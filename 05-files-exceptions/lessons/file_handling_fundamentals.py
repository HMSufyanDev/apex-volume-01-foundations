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

# with
with open("notes.txt", "w", encoding="utf-8") as file:
    file.write("Hello Python")

# .read()
with open("notes.txt", "r", encoding="utf-8") as file:
    content = file.read()
print(content)

# .readline()
# .readline() reads one line.
with open("notes.txt", "r", encoding="utf-8") as file:
    print(file.readline())
    print(file.readline())

# .readlines()
# .readlines() reads all lines and gives you a list.
with open("notes.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

print(lines)

# .write() expects a string
# file.write(100) # Error
file.write(str(100))

# .write() returns something
result = file.write("Hello")
# result is the number of characters written.
with open("notes.txt", "w", encoding="utf-8") as file:
    result = file.write("Hello")
    
print(result) # 5

# .writelines()
# writelines() writes multiple strings.
lines = [
    "Sarah\n", # without \n it does not add new line 
    "Alexandre\n",
    "Amina\n"
]

with open("leads.txt", "w", encoding="utf-8") as file:
    file.writelines(lines)

# File Paths
# Relative Path
# A relative path is a path relative to your current working directory.
open("notes.txt") # Find notes.txt relative to where Python is currently running
open("data/activity.log") # current directory -> data -> activity.log

# Parent Directory: ..
# If you're inside data and want to refer to something in the parent directory:
# ../main.py

# Absolute Path
# An absolute path gives the complete location.
# C:\Users\Sufyan\Documents\Project\data\activity.log

# Current Working Directory
from pathlib import Path
print(Path.cwd()) # C:\Users\Sufyan\Desktop\APEX\week5\day1
open("notes.txt")
# means Python looks around: C:\Users\Sufyan\Desktop\APEX\week5\day1
