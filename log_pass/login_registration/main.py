import Database, random, sys, string

running = True


def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    users = Database.get_accounts()
    if users is not None:
        for accounts in users:
            if accounts.get("username") == username and accounts.get("password") == password:
                print("Welcome", username)
                sys.exit()

    print("Wrong account try again or create a new account")

def random_pass():
    username = input("Enter your username: ")
    second_name = input("Enter your second name: ")
    characters = string.ascii_letters + string.punctuation + string.digits
    password = "".join(random.choice(characters) for a in range(8, 20))
    print(f"Please remember your password: {password}")
    Database.create_account(username, second_name, password)

def own_password():
        username = input("Enter your username: ")
        second_name = input("Enter your second name: ")
        password = input("Enter your password: ")
        Database.create_account(username, second_name, password)

def register():
    print('Do you want to enter the password yourself or use a password generator?')
    print("1. Use my own password")
    print("2. Use a password generator")
    userOption = int(input())
    if userOption == 1:
        own_password()
    if userOption == 2:
        random_pass()


while running:
    print("Welcome to Booking")
    print('Are you already registered in the service or would like to register?')
    print("1. Log in")
    print("2. Create account")
    print("3. Exit")
    userOption = int(input())
    if userOption == 1:
        login()
    if userOption == 2:
        register()
    if userOption == 3:
        running = False