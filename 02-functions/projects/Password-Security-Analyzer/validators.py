def get_valid_password() -> str:
    while True:
        password = input("Enter Your Password: ")
        if not password:
            print("Password cannot be empty, try again!")
            continue
        if " " in password:
            print("Spaces not allowed!, try again!")
            continue

        return password