class AVLTree:
    """
    Self balancing binary search tree (AVL) that is keyed by recipe title
    
    It makes sure it is O(logn) time for the insert, search and delete (add more later)"""

    def __init__(self):
        self.root = None
        self._size = 0

    def __len__(self):
        return self._size

    def (insert, title: str, ingredients: list, instructions: str = ""):
        """insert new recipe into tree by title"""
        self.root = self._insert(self.root, title, ingredients, instructions)
        self._size += 1

    def search(self, title: str) -> RecipeNode | None:
        """search for recipe by exact title and returns RecipeNode if found and doesn't if not"""
        return self._search(self.root, title.lower())

    def search_prefix(self, prefix: str) -> list:
        """return all recipes who titles start with the prefix you give like auto complete and stuff"""
        results = []
        self._search_prefix(self.root, prefix.lower(), results)
        return results
        
    def inorder(self) -> list:
        """return all recipes in alphabet order by title"""
        result = []
        self._inorder(self.root, result)
        return result

    def get_height(self) -> int:
        """return the height of the tree"""
        return self._get_height(self.root)