import getpass
import pymongo

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class LoginSystem:
    def __init__(self, db_uri, db_name, collection_name):
        self.client = pymongo.MongoClient(db_uri)
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]
        self.current_user = None 

    # Add / Register user to database
    def register(self, username, password):
        user = User(username, password)
        user_data = {
            "username": user.username,
            "password": user.password,
        }
        self.collection.insert_one(user_data)
        print(f"User '{username}' registered successfully.")

    # Login user
    def login(self, username, password):                             
        user_data = self.collection.find_one({"username": username})
        if user_data and user_data["password"] == password:
            self.current_user = user_data 
            print(f"Welcome, {username}!")
        else:
            print("Invalid username or password.")

    # Display current user
    def display_current_user(self):
        if self.current_user:
            print("\n**** Current User Information ****")
            print(f"Username: {self.current_user['username']}")
        else:
            print("No user is currently logged in.")

    # Display points of users
    def display_user_points(self, username):
        user_data = self.collection.find_one({"username": username})
        if user_data:
            points = user_data.get("points", 0)
            print(f"User '{username}' has {points} points.")
        else:
            print(f"User '{username}' not found.")

    # Update user's name and password
    def update_user_info(self, username, new_username, new_password):
        user_data = self.collection.find_one({"username": username})

        if user_data:
            # Check if the new username is already taken by another user
            existing_user = self.collection.find_one({"username": new_username})
            if existing_user and existing_user["_id"] != user_data["_id"]:
                print("The new username is already taken. Please choose another one.")
                return

            # Update the user's information
            update_data = {
                "$set": {
                    "username": new_username,
                    "password": new_password
                }
            }
            self.collection.update_one({"_id": user_data["_id"]}, update_data)

            print(f"User '{username}' updated successfully.")
        else:
            print(f"User '{username}' not found.")

    def login_menu(self):
        while True:
            print("\n**** Mcdonald Membership Login ****")
            print("1.Register")
            print("2.Login")
            print("3.Update User Info")
            # print("3.Display User")
            print("4.Display Current Points")
            print("5.Back")

            choice = input("\nSelect an option: ")

            if choice == "1":
                print("\n**** Register Page ****")
                username = input("Enter a username: ")
                password = input("Enter a password: ")
                self.register(username, password)
                
            elif choice == "2":
                print("\n**** Login Page ****")
                username = input("Enter your username: ")
                password = getpass.getpass("Enter your password: ")
                self.login(username, password)

            # elif choice == "3": 
            #     self.display_current_user()

            elif choice == "3":
                if self.current_user:
                    new_username = input("Enter your new username: ")
                    new_password = getpass.getpass("Enter your new password: ")
                    self.update_user_info(self.current_user["username"], new_username, new_password)
                else:
                    print("You need to be logged in to update your information.")

            elif choice == "4":
                username = input("Enter the username to check points: ")
                self.display_user_points(username)

            elif choice == "5":   
                return True
            
            else:
                print("\nInvalid choice.")
