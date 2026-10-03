from loot import Loot
from validators import (
    get_name
)

class LootService:

    def __init__(self) -> None:
        self.loots: list[Loot] = []

    def add_loot(self, id: str, name: str, rarity: str, value: float) -> Loot:
        valid_name = get_name(name)
        
        loot = Loot(
            id,
            valid_name,
            rarity,
            value
        )

        self.loots.append(loot)

        return loot
