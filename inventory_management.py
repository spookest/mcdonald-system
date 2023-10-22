class Ingredients:
    def __init__(self, name, category, quantity):
        self.name = name
        self.category = category
        self.quantity = quantity

    def __str__(self):
        return f"{self.name} ({self.category}) - {self.quantity}"

class InventoryManagementSystem:    
    def __init__(self):
        self.ingredients = []

    def add_ingredients(self, name, category, quantity):
        ingredients = Ingredients(name, category, quantity)
        self.ingredients.append(ingredients)

    def get_all_ingredients(self):
        return self.ingredients
    
def main():
    inventory_system = InventoryManagementSystem()

    while True:
        print("\nInventory Management System")
        print("1. Add Ingredients")
        print("2. View All Ingredients")
        # print("3. View Staff Members by Name")
        # print("4. Update Staff Position")
        # print("5. Delete Staff Member")
        print("6. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            name = input("\nEnter the ingredient name: ")
            category = input("Enter the ingredient category: ")
            quantity = int(input("Enter the quantity: "))
            inventory_system.add_ingredients(name, category, quantity)
            print("Ingredient added successfully!")

        elif choice == "2":
            print("\nAll Ingredients:")
            ingredients = inventory_system.get_all_ingredients()
            for ingredient in ingredients:
                print(ingredient)

        # elif choice == "3":
        #     name = input("Enter the name to search for: ")
        #     matching_ingredients = ingredient_manager.get_ingredient_by_name(name)
        #     print(f"Ingredients with the Name '{name}':")
        #     for ingredient in matching_ingredients:
        #         print(ingredient)

        # elif choice == "4":
        #     name = input("Enter the name of the ingredient to update: ")
        #     new_quantity = int(input("Enter the new quantity: "))
        #     ingredient_manager.update_ingredient(name, new_quantity)
        #     print("Ingredient quantity updated successfully!")

        # elif choice == "5":
        #     name = input("Enter the name of the ingredient to delete: ")
        #     ingredient_manager.delete_ingredient(name)
        #     print("Ingredient deleted successfully!")

        elif choice == "6":
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
        
