def add_activity():
    from datetime import date

    activity = input("Enter activity: ")

    today = date.today()

    with open("data/activity.log", "a", encoding="utf-8") as file:
        file.write(f"[{today}] {activity}\n")


def view_activities():

    with open("data/activity.log", "r", encoding="utf-8") as file:
        content = file.read()

    print(content)



while True:
    print("=" * 40)
    print("CRM Activity Log")
    print("=" * 40)

    print("1. Add activity")
    print("2. View activities")
    print("3. Exit")


    choice = int(input("Choose an option: "))

    if choice == 1:
        add_activity()
    elif choice == 2:
        view_activities()
    elif choice == 3:
        print("Good Bye!")
        break
    else:
        print("Choose valid option")
