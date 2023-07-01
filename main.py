class Snack:
    def __init__(self, snack_id, snack_name, price, availability):
        self.snack_id = snack_id
        self.snack_name = snack_name
        self.price = price
        self.availability = availability


class Canteen:
    def __init__(self):
        self.inventory = {}
        self.sales_records = []

    def add_snack(self, snack):
        self.inventory[snack.snack_id] = snack

    def remove_snack(self, snack_id):
        if snack_id in self.inventory:
            del self.inventory[snack_id]
            print(f"Snack with ID {snack_id} removed from inventory.")
        else:
            print(f"Snack with ID {snack_id} not found in inventory.")

    def update_snack_availability(self, snack_id, availability):
        if snack_id in self.inventory:
            snack = self.inventory[snack_id]
            snack.availability = availability
            print(f"Snack with ID {snack_id} availability updated.")
        else:
            print(f"Snack with ID {snack_id} not found in inventory.")

    def record_sale(self, snack_id):
        if snack_id in self.inventory:
            snack = self.inventory[snack_id]
            if snack.availability == "yes":
                self.sales_records.append(snack)
                snack.availability = "no"
                print(f"Snack with ID {snack_id} sold and inventory updated.")
            else:
                print(f"Snack with ID {snack_id} is currently unavailable.")
        else:
            print(f"Snack with ID {snack_id} not found in inventory.")

    def print_inventory(self):
        print("Current Snack Inventory:")
        for snack in self.inventory.values():
            print(f"ID: {snack.snack_id}, Name: {snack.snack_name}, Price: {snack.price}, Availability: {snack.availability}")

    def print_sales_records(self):
        print("Sales Records:")
        for snack in self.sales_records:
            print(f"ID: {snack.snack_id}, Name: {snack.snack_name}, Price: {snack.price}")


def main():
    canteen = Canteen()

    while True:
        print("\n========== Canteen Management System ==========")
        print("1. Add a snack to inventory")
        print("2. Remove a snack from inventory")
        print("3. Update snack availability")
        print("4. Record a snack sale")
        print("5. Print current inventory")
        print("6. Print sales records")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            snack_id = input("Enter snack ID: ")
            snack_name = input("Enter snack name: ")
            price = input("Enter snack price: ")
            availability = input("Is the snack available? (yes/no): ")
            snack = Snack(snack_id, snack_name, price, availability)
            canteen.add_snack(snack)
            print("Snack added to inventory.")

        elif choice == "2":
            snack_id = input("Enter snack ID to remove: ")
            canteen.remove_snack(snack_id)

        elif choice == "3":
            snack_id = input("Enter snack ID to update availability: ")
            availability = input("Is the snack available? (yes/no): ")
            canteen.update_snack_availability(snack_id, availability)

        elif choice == "4":
            snack_id = input("Enter snack ID sold: ")
            canteen.record_sale(snack_id)

        elif choice == "5":
            canteen.print_inventory()

        elif choice == "6":
            canteen.print_sales_records()

        elif choice == "0":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
