from loot_service import LootService


# ========================================
# Loot Management

def add_loot(loot) -> None:

    while True:
        try:

            name = input("Enter name: ").strip().capitalize()
            rarity = input("Enter rarity: ").strip().capitalize()
            value = float(input("Enter value: "))

            loot = loot.add_loot(name, rarity, value)

            print(loot)

            break

        except ValueError as error:
            print(error)

def view_inventory(loot) -> None:
    loot.view_inventory()

def search_loot(loot):

    while True:
        try:
            query = input("Enter Loot Name: ").strip().lower()
            available_loots = loot.search_loot(query)

            if not available_loots:
                print("\nNo loot found matching your query!")
                return

            print(f"\n--- Search Results ({len(available_loots)}) ---")
            for loot in available_loots:
                print(loot)

            break

        except ValueError as error:
            print(error)


def rare_loot(loot) -> None:
    rare_loots = loot.rare_loot()

    if not rare_loots:
        print("\nNo rare loot found!")
        return

    for loot in rare_loots:
        print(loot)


def inventory_value(loot) -> None:

    value: float = loot.inventory_value()

    print(f"${value}")
    


# ========================================



def display_menu() -> None:
    
    print("\n🎮 GAME LOOT TRACKER")
    print("1. Add Loot")
    print("2. View Inventory")
    print("3. Search Loot")
    print("4. Show Rare Loot")
    print("5. Show Inventory Value")
    print("6. Remove Loot")
    print("7. Exit")
    print()


def main() -> None:

    loot = LootService()

    while True:

        display_menu()

        choose: int = int(input("Choose: "))
        print()

        if choose == 1:
            add_loot(loot)
        elif choose == 2:
            view_inventory(loot)
        elif choose == 3:
            search_loot(loot)
        elif choose == 4:
            rare_loot(loot)
        elif choose == 5:
            inventory_value(loot)
        elif choose == 6:
            pass
        elif choose == 7:
            break
        else:
            pass

if __name__ == "__main__":
    main()