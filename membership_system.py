class Customer:
    def __init__(self, name, initial_points=0):
        self.name = name
        self.points = initial_points

    def purchase_food(self, food_name, price):
        if self.points >= price:
            self.points -= price
            print(f"{self.name} purchased {food_name} for {price} points.")
        else:
            print(f"{self.name} does not have enough points to purchase {food_name}.")

    def earn_points(self, amount):
        self.points += amount

    def check_points(self):
        return self.points

class Food:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class MembershipSystem:
    def __init__(self):
        self.customers = []
        self.food_menu = []

    def add_customer(self, customer):
        self.customers.append(customer)

    def add_food_item(self, food_item):
        self.food_menu.append(food_item)

    def display_menu(self):
        print("Food Menu:")
        for food_item in self.food_menu:
            print(f"{food_item.name}: {food_item.price} points")

    def redeem_food(self, customer_name, food_name):
        customer = None
        for c in self.customers:
            if c.name == customer_name:
                customer = c
                break

        food = None
        for f in self.food_menu:
            if f.name == food_name:
                food = f
                break

        if customer and food:
            customer.purchase_food(food.name, food.price)
        else:
            print("Customer or food not found.")

def main():
    membership_system = MembershipSystem()

    while True:
        print("\nChoose an option:")
        print("1. Add Customer")
        print("2. Add Food Item")
        print("3. Display Menu")
        print("4. Earn Points")
        print("5. Redeem Food")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter customer's name: ")
            initial_points = int(input("Enter initial points (default is 0): "))
            customer = Customer(name, initial_points)
            membership_system.add_customer(customer)
            print(f"{name} added as a customer!")

        elif choice == "2":
            name = input("Enter food item name: ")
            price = int(input("Enter price in points: "))
            food_item = Food(name, price)
            membership_system.add_food_item(food_item)
            print(f"{name} added to the food menu!")

        elif choice == "3":
            membership_system.display_menu()

        elif choice == "4":
            name = input("Enter customer's name: ")
            points = int(input("Enter points earned: "))
            for customer in membership_system.customers:
                if customer.name == name:
                    customer.earn_points(points)
                    print(f"{points} points earned by {name}.")
                    break
            else:
                print("Customer not found.")

        elif choice == "5":
            customer_name = input("Enter customer's name: ")
            food_name = input("Enter food item name: ")
            membership_system.redeem_food(customer_name, food_name)

        elif choice == "6":
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
