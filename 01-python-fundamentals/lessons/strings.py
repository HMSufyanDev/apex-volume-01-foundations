# Indexing
name: str = "Sufyan"
print(name[0]) # S

# Negative indexing
print(name[-1]) # n

# Slicing
name: str = "Sufyan"
print(name[0:3]) # Suf
print(name[:3]) # Suf
print(name[3:]) # yan
print(name[:]) # whole string

# Slicing with a step
# string[start:end:step]
name: str = "Sufyan"
print(name[::2]) # This takes every second character. # Sfa

# Strings are immutable
# name: str = "Sufyan"
# name[0] = "X" This is not allowed

# Instead, you create a new string:
name: str = "Sufyan"
name = "X" + name[1:]
print(name) # Xufyan

# strip(): strip() removes whitespace from the beginning and end of a string.
name: str = "   Sufyan   "
clean_name: str = name.strip()
print(clean_name)

# lower()
email: str = "CLIENT@EXAMPLE.COM"
print(email.lower())

# upper()
name: str = "sufyan"
print(name.upper())

# replace()
message: str = "I like Python"
new_message: str = message.replace("Python", "AI")
print(new_message)

phone: str = "0300-123-4567"
clean_phone: str = phone.replace("-", "")
print(clean_phone)

# split()
sentence: str = "Python is powerful"
words = sentence.split()
print(words) # ['Python', 'is', 'powerful']

# split() with a separator
email: str = "sufyan@example.com"
parts = email.split("@")
print(parts) # ['sufyan', 'example.com']

# join()
words: list[str] = ["Python", "is", "powerful"]
sentence: str = " ".join(words)
print(sentence) # Python is powerful
# The " " means: Put a space between each item.

# f-strings
client_name: str = "James"
price: int = 500
# You want: Hi James, your website quotation is $500.
message: str = f"Hi {client_name}, your website quotation is ${price}."
print(message)