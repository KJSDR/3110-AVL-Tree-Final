import json
from src.avl_tree import AVLTree


class RecipeStore:
    """loads th recipe JSON files and stores them in an AVL tree keyed by title"""

    def __init__(self):
        self.tree = AVLTree()

    def load(self, filepath: str):
        """load JSON file and insert each recipe into tree"""
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)

        for key, recipe in data.items():
            title = recipe.get('title', '').strip()
            ingredients = recipe.get('ingredients', [])
            instructions = recipe.get('instructions', '')

            #skip any recipes that dont have title
            if not title:
                continue

            self.tree.insert(title, ingredients, instructions)

        print(f"Loaded {filepath} — tree now has {len(self.tree)} recipes")

    def search(self, title: str):
        """search for recipe by exact title"""
        return self.tree.search(title)

    def search_prefix(self, prefix: str):
        """return all recipes who title starts with the given prefix"""
        return self.tree.search_prefix(prefix)

    def all_recipes(self):
        """return all recipes in alphabet order"""
        return self.tree.inorder()

    def stats(self):
        """print basic stats about the tree"""
        print(f"Total recipes: {len(self.tree)}")
        print(f"Tree height:   {self.tree.get_height()}")