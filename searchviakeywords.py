recipe_name = input('Enter your recipe name: ')
recipe_region = input("Enter the recipes' region: ")
recipe_culture = input('What culture is this recipe from: ')
data_list = [
    [recipe_name, recipe_region, recipe_culture,]
    ['Meat Cholent', 'Africa', 'Morrocan',]
    ['Vegetarian Cholent' 'Not Africa', 'Not Morrocan']
]

def add_item():
    item = input("Enter an item to add: ")
    data_list.append(item)
    print(f'"{item}" added to the list')


def search_items():
    keyword = input("Enter a keyword to search: ").lower()
    results = [item for item in data_list if keyword in item.lower()]

    if results:
        print("Search results:")
        for res in results:
            print(f"- {res}")
    else:
        print("No matches found.")


# Menu loop
while True:
    print("\nOptions: (1) Add Item, (2) Search, (3) Show List, (4) Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        add_item()
    elif choice == "2":
        search_items()
    elif choice == "3":
        print("Current List:", data_list)
    elif choice == "4":
        print("Goodbye")
        break
    else:
        print("Invalid choice, try again.")