def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")


def main():
    shopping_list = []  # REQUIRED array/list name

    while True:
        display_menu()   # REQUIRED: call of display_menu

        try:
            choice = int(input("Enter your choice: "))  # REQUIRED: input as NUMBER
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == 1:
            item = input("Enter item to add: ")
            shopping_list.append(item)
            print(f"{item} added.")

        elif choice == 2:
            item = input("Enter item to remove: ")
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"{item} removed.")
            else:
                print("Item not found.")

        elif choice == 3:
            print("Current Shopping List:")
            for item in shopping_list:
                print(item)

        elif choice == 4:
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
