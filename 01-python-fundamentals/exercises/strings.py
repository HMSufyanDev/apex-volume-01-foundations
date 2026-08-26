# Exercise 1 — Normalize a person's name

name: str = "   jAmEs sMiTh   "
name = name.strip().lower().title()
print(name)

# Exercise 2 — Extract a domain from an email
email: str = "client@example.com"
domain = email.split("@")[1]
print(domain)

# Exercise 3 — Count words
sentence: str = "Python makes software development powerful"
sentence_split = sentence.split()
word_count = len(sentence_split)
print(word_count) # 5

# Exercise 4 — Invoice message
client_name: str = "James"
price: int = 500
messsage: str = f"Hi, {client_name}, your website quotation is ${price}."
print(messsage)

# Exercise 5 — Hide part of a phone number
phone: str = "03001234567"
# Slicing the first 4 characters, adding 6 asterisks, and slicing the last 2 characters
masked_phone = phone[:4] + "*" * 6 + phone[-2:]
print(masked_phone) # 0300******67