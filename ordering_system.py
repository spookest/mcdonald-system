class OrderingSystem:
    def __init__(self, current_user=None):
        self.menu = {
            "Burger": 5,
            "Fries": 3,
            "Soda": 2,
            "Ice Cream": 4,
        }
        self.cart = {}
        self.current_user = current_user

    def display_menu(self):
        print("\n**** Menu *************")
        for item, points in self.menu.items():
            print(f"{item: <15}{points} points")
        print("***********************")

    def purchase_item(self, item, quantity):
        if item in self.menu:
            if item in self.cart:
                self.cart[item] += quantity
            else:
                self.cart[item] = quantity
            print(f"Purchased {quantity} {item}(s).")

    def calculate_total_points(self):
        total_points = 0
        for item, quantity in self.cart.items():
            if item in self.menu:
                total_points += self.menu[item] * quantity
        return total_points

    def view_cart(self):
        print("Cart Contents:")
        for item, quantity in self.cart.items():
            print(f"{item} - {quantity}")
        print(f"Total Points: {self.calculate_total_points()} points")

    def checkout(self, login_system):
        total_points = self.calculate_total_points()

        if not login_system.current_user:
            print("You must log in first.")
            return

        username = login_system.current_user['username']
        login_system.update_user_points(username, total_points)
        print(f"Thank you for your order! Total points: {total_points} points")
        self.cart = {}


def order_menu(login_system, order_system):
    current_user = login_system.current_user
    while True:
        if current_user:
            print(f"Current User: {current_user['username']}")
        else:
            print("Not currently logged in")

        print("\n**** Ordering System ****")
        print("1. Display Menu")
        print("2. Order a Meal")
        print("3. View Cart")
        print("4. Checkout")
        print("5. Back")
        choice = input("\nSelect an option: ")

        if choice == "1":
            order_system.display_menu()

        elif choice == "2":
            if not current_user:
                print("You must log in first.")
            else:
                item = input("Enter the item you want to purchase: ")
                quantity = int(input(f"How many {item} do you want to buy? "))
                order_system.purchase_item(item, quantity)

        elif choice == "3":
            if not current_user:
                print("You must log in first.")
            else:
                order_system.view_cart()

        elif choice == "4":
            if not current_user:
                print("You must log in first.")
            else:
                order_system.checkout(login_system)

        elif choice == "5":
            return True

        else:
            print("\nInvalid choice.")
