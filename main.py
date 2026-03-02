from src.recipe_store import RecipeStore


def display_recipe(node):
    """print single recipe"""
    print(f"\n{'='*50}")
    print(f"  {node.title}")
    print(f"{'='*50}")
    print("Ingredients:")
    for ingredient in node.ingredients:
        print(f"  - {ingredient}")
    if node.instructions:
        print(f"\nInstructions:\n  {node.instructions[:300]}...")
    print()


def main():
    store = RecipeStore()

    # load both datasets into the same tree
    store.load("data/recipes_raw_nosource_epi.json")
    store.load("data/recipes_raw_nosource_fn.json")

    store.stats()

    while True:
        print("\nWhat do you want to do?")
        print("  1. Search by exact title")
        print("  2. Search by prefix (autocomplete)")
        print("  3. List all recipes A-Z")
        print("  4. Quit")

        choice = input("\nEnter choice: ").strip()

        if choice == "1":
            title = input("Enter recipe title: ").strip()
            result = store.search(title)
            if result:
                display_recipe(result)
            else:
                print(f"No recipe found for '{title}'")

        elif choice == "2":
            prefix = input("Enter prefix: ").strip()
            results = store.search_prefix(prefix)
            if results:
                print(f"\nFound {len(results)} recipes starting with '{prefix}':")
                for node in results:
                    print(f"  - {node.title}")
            else:
                print(f"No recipes found starting with '{prefix}'")

        elif choice == "3":
            recipes = store.all_recipes()
            print(f"\nAll {len(recipes)} recipes in alphabetical order:")
            for node in recipes:
                print(f"  - {node.title}")

        elif choice == "4":
            print("Bye!")
            break

        else:
            print("Invalid choice, try again")


if __name__ == "__main__":
    main()