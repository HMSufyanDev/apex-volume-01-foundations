from loot_service import LootService


# ========================================
# Loot Management

loot_counter = 0

def add_loot(loot) -> None:

    while True:
        try:
            global loot_counter
            loot_counter += 1

            loot_id = f"L{loot_counter:03d}"

            name = input("Enter name: ").strip()
            rarity = input("Enter rarity: ").strip()
            value = float(input("Enter value: "))

            loot = loot.add_loot(loot_id, name, rarity, value)

            print(loot)

            break

        except ValueError as error:
            print(error)



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


def main() -> None:

    loot = LootService()

    while True:

        display_menu()

        choose: int = int(input("Choose: "))

        if choose == 1:
            add_loot(loot)
        elif choose == 2:
            pass
        elif choose == 3:
            pass
        elif choose == 4:
            pass
        elif choose == 5:
            pass
        elif choose == 6:
            pass
        elif choose == 7:
            break
        else:
            pass

if __name__ == "__main__":
    main()