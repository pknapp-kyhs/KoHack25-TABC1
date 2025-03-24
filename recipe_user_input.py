def search_recipes_by_keywords():
    """Search for recipes based on keywords."""
    recipes_db = [
        {"name": "Spicy Shakshuka", "ingredients": ["eggs", "tomatoes", "peppers"], "cuisine": "Middle Eastern"},
        {"name": "Chocolate Babka", "ingredients": ["chocolate", "flour", "yeast"], "cuisine": "Jewish"},
        {"name": "Matzah Brei", "ingredients": ["matzah", "eggs", "butter"], "cuisine": "Ashkenazi"},
        {"name": "Falafel", "ingredients": ["chickpeas", "tahini", "garlic"], "cuisine": "Middle Eastern"},
        {"name": "Potato Kugel", "ingredients": ["potatoes", "onion", "eggs"], "cuisine": "Jewish"},
        {"name": "Cheese Bourekas", "ingredients": ["cheese", "phyllo dough", "butter"], "cuisine": "Sephardi"},
        {"name": "Cholent", "ingredients": ["beef", "potatoes", "barley"], "cuisine": "Ashkenazi"},
    ]

    while True:
        keywords = input(
            "\nEnter keywords to search for a recipe (separate by commas) or type 'exit' to quit: ").strip().lower()

        if keywords == "exit":
            print("\nGoodbye! Happy cooking!")
            break  # Exit the loop and end the program

        keywords = [kw.strip() for kw in keywords.split(",")]  # Remove extra spaces

        matching_recipes = []

        for recipe in recipes_db:
            if any(kw in recipe["name"].lower() or kw in recipe["cuisine"].lower() or kw in " ".join(
                    recipe["ingredients"]).lower() for kw in keywords):
                matching_recipes.append(recipe)

        if matching_recipes:
            print("\nMatching recipes:")
            for recipe in matching_recipes:
                print(f"- {recipe['name']} ({recipe['cuisine']}) - Ingredients: {', '.join(recipe['ingredients'])}")
        else:
            print("\nNo recipes matched your keywords. Try again.")

        # Return to the main menu after search
        return  # Exit the search function and return to the main menu


def get_valid_input(prompt, allow_numbers=False):
    """Get user input and ensure it doesn't contain numbers if not allowed."""
    while True:
        user_input = input(prompt).strip()
        if not allow_numbers and any(char.isdigit() for char in user_input):
            print("Numbers are not allowed. Please try again.")
        else:
            return user_input


def get_allergies():
    """Ask user about allergies and return a list of selected ones"""
    allergies = ["Nuts", "Gluten", "Dairy", "Soy", "Eggs",]
    selected_allergies = []

    while True:
        print("\nDo you have any allergies? (Select multiple by entering numbers separated by spaces)")
        for i, allergy in enumerate(allergies, start = 1):
            print(f"{i}. {allergy}")

        choices = input("Enter numbers corresponding to your allergies (or press Enter to skip): ").split()

        if all(choice.isdigit() and 1 <= int(choice) <= len(allergies) for choice in choices):
            selected_allergies = [allergies[int(choice) - 1] for choice in choices]
            break
        else:
            print("Invalid input. Please enter numbers from the list, separated by spaces.")

    return selected_allergies


def get_ingredients():
    """Allow user to enter multiple ingredients (without numbers)."""
    ingredients = []
    print("\nEnter ingredients (type 'done' when finished):")
    while True:
        ingredient = get_valid_input("Ingredient: ", allow_numbers=False)
        if ingredient.lower() == "done":
            break
        ingredients.append(ingredient)
    return ingredients


def get_holiday():
    """Ask user which Jewish holiday the recipe is associated with"""
    holidays = ["Pesach", "Shavuos", "Chanukah", "Sukkos", "Rosh Hashanah", "Purim", "General (Not Specific)"]

    while True:
        print("\nWhich Jewish holiday is this recipe associated with?")
        for i, holiday in enumerate(holidays, start=1):
            print(f"{i}. {holiday}")

        choice = input("Enter the number corresponding to the holiday: ")

        if choice.isdigit() and 1 <= int(choice) <= len(holidays):
            return holidays[int(choice) - 1]
        else:
            print("Invalid choice. Please enter a number from the list.")


def add_recipe(recipes):
    """Ask user for a new recipe and add it to the list"""
    while True:
        name = get_valid_input("\nEnter recipe name: ", allow_numbers=False)
        if any(char.isdigit() for char in name):
            print("Invalid input. Recipe name cannot contain numbers. Please enter a valid name.")
        else:
            break

    while True:
        origin = get_valid_input("Enter recipe origin (location): ", allow_numbers=False)
        if any(char.isdigit() for char in origin):
            print("Invalid input. Origin location cannot contain numbers. Please enter a valid location.")
        else:
            break

    while True:
        culture = input("Enter the recipe's cultural background (1 for Ashkenazi, 2 for Sephardi): ")
        if culture == "1":
            culture = "Ashkenazi"
            break
        elif culture == "2":
            culture = "Sephardi"
            break
        else:
            print("Invalid choice. Please enter 1 for Ashkenazi or 2 for Sephardi.")

    while True:
        category = input("Is this recipe Meat, Dairy, or Parve? ").strip().capitalize()
        if category in ["Meat", "Dairy", "Parve"]:
            break
        print("Invalid input. Please enter 'Meat', 'Dairy', or 'Parve'.")

    holiday = get_holiday()
    allergies = get_allergies()
    ingredients = get_ingredients()

    # New feature: Ask for special instructions
    special_instructions = input("\nEnter instructions for making this recipe (or press Enter to skip): ").strip()

    recipes.append({
        "name": name,
        "origin": origin,
        "culture": culture,
        "category": category,
        "holiday": holiday,
        "allergies": allergies,
        "ingredients": ingredients,
        "special_instructions": special_instructions  # Add special instructions to the recipe
    })
    print(f"\n'{name}' has been added to the database!")


def browse_recipes(recipes):
    """Allow user to browse recipes based on dietary, cultural, and holiday preferences"""

    while True:
        category = input("\nWhat type of food are you looking for? Choose Meat, Dairy, or Parve: ").strip().capitalize()
        if category in ["Meat", "Dairy", "Parve"]:
            break
        print("Invalid input. Please enter 'Meat', 'Dairy', or 'Parve'.")

    user_allergies = get_allergies()

    while True:
        culture_preference = input(
            "\nWould you like Ashkenazi or Sephardi food? (Enter 1 for Ashkenazi, 2 for Sephardi, or 'Any'): ").strip()
        if culture_preference == "1":
            culture_preference = "Ashkenazi"
            break
        elif culture_preference == "2":
            culture_preference = "Sephardi"
            break
        elif culture_preference.lower() == "any":
            culture_preference = "Any"
            break
        else:
            print("Invalid choice. Please enter 1 for Ashkenazi, 2 for Sephardi, or 'Any'.")

    while True:
        holiday_preference = input(
            "\nAre you looking for a recipe for a specific Jewish holiday? (Yes/No): ").strip().lower()
        if holiday_preference == "yes":
            holiday = get_holiday()
            break
        elif holiday_preference == "no":
            holiday = "Any"
            break
        else:
            print("Invalid input. Please enter 'Yes' or 'No'.")

    print("\nMatching recipes:")
    found = False
    for recipe in recipes:
        if recipe["category"] == category and (culture_preference == "Any" or recipe["culture"] == culture_preference):
            if any(allergy in recipe["allergies"] for allergy in user_allergies):
                continue
            if holiday == "Any" or recipe["holiday"] == holiday:
                print(
                    f"- {recipe['name']} ({recipe['origin']}, {recipe['culture']}) [{recipe['category']}] - Holiday: {recipe['holiday']} - Ingredients: {', '.join(recipe['ingredients'])} - Special Instructions: {recipe['special_instructions']}")
                found = True

    if not found:
        print("No recipes matched your preferences.")


def main():
    """Main program loop"""
    recipes_db = []

    while True:
        choice = input(
            "\nWould you like to (1) Input a Recipe, (2) Browse Recipes, (3) Search Recipes by Keywords, or 'exit' to quit: ").strip().lower()

        if choice == "1":
            add_recipe(recipes_db)
        elif choice == "2":
            browse_recipes(recipes_db)
        elif choice == "3":
            search_recipes_by_keywords()
        elif choice == "exit":
            print("\nGoodbye! Happy cooking!")
            break
        else:
            print("Invalid option. Please choose a valid action.")