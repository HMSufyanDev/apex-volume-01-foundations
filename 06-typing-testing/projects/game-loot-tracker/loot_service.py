from loot import Loot
from validators import (
    get_name,
    validate_positive,
    validate_rarity
)

class LootService:

    def __init__(self) -> None:
        self.loots: list[Loot] = []
        self.loot_counter: int = 0


    def add_loot(self, name: str, rarity: str, value: float) -> Loot:

        valid_name = get_name(name)
        valid_rarity = validate_rarity(rarity)
        valid_positive = validate_positive(value)

        self.loot_counter += 1

        id = f"L{self.loot_counter:03d}"


        loot = Loot(
            id,
            valid_name,
            valid_rarity,
            valid_positive
        )

        self.loots.append(loot)

        return loot
