class Loot:

    def __init__(self, id: str, name: str, rarity: str, value: float) -> None:
        self.id = id
        self.name = name
        self.rarity = rarity
        self.value = value


    def __str__(self):
        return f"\n ID: {self.id} | Name: {self.name} | Rarity: {self.rarity} | Value: {self.value:.2f} \n"
