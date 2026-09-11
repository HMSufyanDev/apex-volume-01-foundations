# Sort Clients by Price
clients = [
    {"name": "Client A", "price": 500},
    {"name": "Client B", "price": 1200},
    {"name": "Client C", "price": 800}
]

sorted_clients = list(sorted(
    clients,
    key=lambda client: client["price"]
))



# Word Frequency Counter
text = "python data python lists data python"
text_list = text.split()

word_frequency = {}
for word in text_list:
    if word not in word_frequency:
        word_frequency[word] = 0
    word_frequency[word] += 1

print(word_frequency)