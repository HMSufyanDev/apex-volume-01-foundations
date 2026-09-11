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

