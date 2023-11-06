from login_system import LoginSystem
from ordering_system import OrderingSystem, order_menu

def main():
    db_uri = "mongodb+srv://dev:123@mcdonald-system.qwbro0h.mongodb.net/"   # MongoDB connection URI
    db_name = "mcdonald-system"                                             # MongoDB database name
    collection_name = "users"                                               # Collection name

    login_system = LoginSystem(db_uri, db_name, collection_name)
    order_system = OrderingSystem()

    while True:
        if login_system.current_user:
            print(f"Current User: {login_system.current_user['username']}")
        else:
            print("Not currently logged in")

        print("\n**** McDonald System ****")
        print("1. Login System")
        print("2. Order a Meal")
        print("3. Exit")
        choice = input("\nSelect an option: ")

        if choice == "1":
            login_system.login_menu()

        elif choice == "2":
            if not login_system.current_user:
                print("You must log in first.")
            else:
                order_menu(login_system, order_system)

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
