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

    def view_inventory(self) -> None:
        for loot in self.loots:
            print(loot)

    def search_loot(self, query) -> list[Loot]:

        validate_query = get_name(query)

        return [loot for loot in self.loots if validate_query in loot.name.lower()]

    def rare_loot(self) -> list[Loot]:

        RARE_LOOTS = {
            "Epic",
            "Legendary"
        }

        return [loot for loot in self.loots if loot.rarity in RARE_LOOTS]

    def inventory_value(self) -> float:

        return sum(
            [loot.value for loot in self.loots]
        )


    def remove_loot(self, choose) -> Loot:

        loot = self.loots.pop(choose - 1)
        return loot 
