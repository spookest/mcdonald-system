class Staff:
    def __init__(self, name, position, employee_id):
        self.name = name
        self.position = position
        self.employee_id = employee_id

    def __str__(self):
        return f"Name: {self.name}, Position: {self.position}, Employee ID: {self.employee_id}"

class StaffManagementSystem:
    def __init__(self):
        self.staff_list = []

    def create_staff(self, name, position, employee_id):
        staff_member = Staff(name, position, employee_id)
        self.staff_list.append(staff_member)

    def get_all_staff(self):
        return self.staff_list

    def get_staff_by_name(self, starting_letter):
        matching_staff = []
        for staff in self.staff_list:
            if staff.name.startswith(starting_letter):
                matching_staff.append(staff)
        return matching_staff

    def update_staff(self, employee_id, new_position):
        for staff in self.staff_list:
            if staff.employee_id == employee_id:
                staff.position = new_position
                break

    def delete_staff(self, employee_id):
        updated_staff_list = []
        for staff in self.staff_list:
            if staff.employee_id != employee_id:
                updated_staff_list.append(staff)
        self.staff_list = updated_staff_list

def main():
    staff_system = StaffManagementSystem()

    while True:
        print("\nStaff Management System")
        print("1. Create Staff")
        print("2. View All Staff Members")
        print("3. View Staff Members by Name")
        print("4. Update Staff Position")
        print("5. Delete Staff Member")
        print("6. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            name = input("\nEnter the name of the staff member: ")
            position = input("Enter the position of the staff member: ")
            employee_id = int(input("Enter the employee ID: "))

            # Check for duplicate employee IDs
            if not any(staff.employee_id == employee_id for staff in staff_system.get_all_staff()):
                staff_system.create_staff(name, position, employee_id)
                print("Staff member created.")
            else:
                print("Employee ID already exists. Please use a unique ID.")

        elif choice == "2":
            print("\nAll Staff Members:")
            all_staff = staff_system.get_all_staff()
            for staff in all_staff:
                print(f"  {staff}")

        elif choice == "3":
            starting_letter = input("\nEnter the starting letter of the name to search for: ")
            matching_staff = staff_system.get_staff_by_name(starting_letter)
            print(f"Staff Members with Names Starting with '{starting_letter}':")
            
            if matching_staff:
                for staff in matching_staff:
                    print(f"  {staff.name}, {staff.position}, Employee ID: {staff.employee_id}")
            else:
                print("No staff members found with names starting with the specified letter.")

        elif choice == "4":
            employee_id = int(input("\nEnter the employee ID to update position: "))
            new_position = input("Enter the new position: ")
            staff_system.update_staff(employee_id, new_position)
            print("Staff member position updated.")

        elif choice == "5":
            employee_id = int(input("\nEnter the employee ID to delete: "))
            staff_system.delete_staff(employee_id)
            print("Staff member deleted.")

        elif choice == "6":
            print("\nExiting the Staff Management System. Goodbye!")
            break

        else:
            print("\nInvalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
