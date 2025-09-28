def display_menu():
    # Use f-string and the specific characters mentioned
    print(f"Shopping/s List/s*Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            item_to_add = input("Enter item to add: ")
            shopping_list.append(item_to_add)
            print(f"Added {item_to_add} to the list.")
        elif choice == '2':
            item_to_remove = input("Enter item to remove: ")
            if item_to_remove in shopping_list:
                shopping_list.remove(item_to_remove)
                print(f"Removed {item_to_remove} from the list.")
            else:
                print(f"{item_to_remove} not found in the list.")
        elif choice == '3':
            print("Current shopping list:")
            if not shopping_list:
                print("The list is currently empty.")
            else:
                for item in shopping_list:
                    print(f"- {item}")
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

if __name__ == "__main__":

    main()


