from __future__ import annotations
from src.avl_node import RecipeNode


class AVLTree:
    """self balancing binarysearch tree keyed by recipe title it guarantees O(logn) for insert search and traversal"""

    def __init__(self):
        self.root = None
        self._size = 0

    def __len__(self):
        return self._size

    #public methods

    def insert(self, title: str, ingredients: list, instructions: str = ""):
        """insert a new recipe into the tree by title"""
        self.root = self._insert(self.root, title, ingredients, instructions)
        self._size += 1

    def search(self, title: str) -> RecipeNode | None:
        """search by exact title returns RecipeNode or none"""
        return self._search(self.root, title.lower())

    def search_prefix(self, prefix: str) -> list:
        """returns all recipes whose title starts with prefix like autocomplete"""
        results = []
        self._search_prefix(self.root, prefix.lower(), results)
        return results

    def inorder(self) -> list:
        """returns all recipes in alphabetical order"""
        result = []
        self._inorder(self.root, result)
        return result

    def get_height(self) -> int:
        """returns height of the tree"""
        return self._get_height(self.root)

    #height and balance helpers

    def _get_height(self, node: RecipeNode | None) -> int:
        if node is None:
            return 0
        return node.height

    def _update_height(self, node: RecipeNode):
        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))

    def _balance_factor(self, node: RecipeNode) -> int:
        #positive = left heavy and negative = right heavy 0 = balanced
        if node is None:
            return 0
        return self._get_height(node.left) - self._get_height(node.right)

    #rotations

    def _rotate_right(self, z: RecipeNode) -> RecipeNode:
        #fixes left-left imbalance
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        self._update_height(z)
        self._update_height(y)
        return y

    def _rotate_left(self, z: RecipeNode) -> RecipeNode:
        #fixes right-right imbalance
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        self._update_height(z)
        self._update_height(y)
        return y

    def _rebalance(self, node: RecipeNode, key: str) -> RecipeNode:
        bf = self._balance_factor(node)

        #left-left
        if bf > 1 and key < node.left.title.lower():
            return self._rotate_right(node)

        #right-right
        if bf < -1 and key > node.right.title.lower():
            return self._rotate_left(node)

        #left-right
        if bf > 1 and key > node.left.title.lower():
            node.left = self._rotate_left(node.left)
            return self._rotate_right(node)

        #right-left
        if bf < -1 and key < node.right.title.lower():
            node.right = self._rotate_right(node.right)
            return self._rotate_left(node)

        return node

    #recursive ops

    def _insert(self, node: RecipeNode | None, title: str, ingredients: list, instructions: str) -> RecipeNode:
        if node is None:
            return RecipeNode(title, ingredients, instructions)

        key = title.lower()
        node_key = node.title.lower()

        if key < node_key:
            node.left = self._insert(node.left, title, ingredients, instructions)
        elif key > node_key:
            node.right = self._insert(node.right, title, ingredients, instructions)
        else:
            #duplicate title and just update data
            node.ingredients = ingredients
            node.instructions = instructions
            self._size -= 1
            return node

        self._update_height(node)
        return self._rebalance(node, key)

    def _search(self, node: RecipeNode | None, key: str) -> RecipeNode | None:
        if node is None:
            return None
        node_key = node.title.lower()
        if key == node_key:
            return node
        elif key < node_key:
            return self._search(node.left, key)
        else:
            return self._search(node.right, key)

    def _search_prefix(self, node: RecipeNode | None, prefix: str, results: list):
        if node is None:
            return
        node_key = node.title.lower()
        if node_key >= prefix:
            self._search_prefix(node.left, prefix, results)
        if node_key.startswith(prefix):
            results.append(node)
        if node_key <= prefix or node_key.startswith(prefix):
            self._search_prefix(node.right, prefix, results)

    def _inorder(self, node: RecipeNode | None, result: list):
        if node is None:
            return
        self._inorder(node.left, result)
        result.append(node)
        self._inorder(node.right, result)