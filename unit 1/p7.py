

my_list = []

while True:
    print("\n--- LIST OPERATIONS MENU ---")
    print("1. Add element")
    print("2. Insert element at position")
    print("3. Delete element")
    print("4. Display list")
    print("5. Sort list")
    print("6. Search element")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        item = input("Enter element to add: ")
        my_list.append(item)
        print("Element added successfully.")

    elif choice == 2:
        item = input("Enter element to insert: ")
        pos = int(input("Enter position: "))
        my_list.insert(pos, item)
        print("Element inserted successfully.")

    elif choice == 3:
        item = input("Enter element to delete: ")
        if item in my_list:
            my_list.remove(item)
            print("Element deleted successfully.")
        else:
            print("Element not found.")

    elif choice == 4:
        print("List elements:", my_list)

    elif choice == 5:
        my_list.sort()
        print("List sorted successfully.")

    elif choice == 6:
        item = input("Enter element to search: ")
        if item in my_list:
            print("Element found at position:", my_list.index(item))
        else:
            print("Element not found.")

    elif choice == 7:
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Please try again.")
