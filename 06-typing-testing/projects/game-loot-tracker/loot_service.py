from loot import Loot

class LootService:

    def __init__(self) -> None:
        self.loots: list[Loot] = []

    def add_loot(self, id: str, name: str, rarity: str, value: float) -> Loot:

        loot = Loot(
            id,
            name,
            rarity,
            value
        )

        self.loots.append(loot)

        return loot
