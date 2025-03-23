print("\nRecipes:")
print("1. Add item")
print("2. Search item")
print("3. Exit")

choice = input("Enter your choice (1-3): ")

if choice == "1":
    print("You chose to add an item.")
elif choice == "2":
    print("You chose to search for an item.")
elif choice == "3":
    print("Goodbye!")
else:
    print("Invalid choice. Please try again.")
