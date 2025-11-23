def display_menu():
    print("shopping_list_manager")
    print(" 1 add an item ")
    print("2 remove item ")
    print("view list")
    print("4. exit ")
def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
           
            pass
        elif choice == '2':
           
            pass
        elif choice == '3':
            # Display the shopping list
            pass
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()