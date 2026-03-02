from __future__ import annotations
import unittest
from src.avl_tree import AVLTree


class TestAVLTree(unittest.TestCase):

    def setUp(self):
        """Fresh tree before each test."""
        self.tree = AVLTree()
        self.tree.insert("Chocolate Cake", ["flour", "sugar", "cocoa"], "Mix and bake.")
        self.tree.insert("Apple Pie", ["apples", "sugar", "pastry"], "Fill and bake.")
        self.tree.insert("Banana Bread", ["bananas", "flour", "butter"], "Mash and bake.")
        self.tree.insert("Zucchini Soup", ["zucchini", "broth", "garlic"], "Simmer.")
        self.tree.insert("Egg Salad", ["eggs", "mayo", "mustard"], "Mix together.")

    #basic insert
    def test_insert_size(self):
        self.assertEqual(len(self.tree), 5)

    def test_insert_duplicate_does_not_increase_size(self):
        self.tree.insert("Apple Pie", ["apples"], "Updated.")
        self.assertEqual(len(self.tree), 5)

    #search

    def test_search_existing_recipe(self):
        result = self.tree.search("Apple Pie")
        self.assertIsNotNone(result)
        self.assertEqual(result.title, "Apple Pie")

    def test_search_case_insensitive(self):
        result = self.tree.search("apple pie")
        self.assertIsNotNone(result)

    def test_search_nonexistent_recipe(self):
        result = self.tree.search("Fish Tacos")
        self.assertIsNone(result)

    #prefix search

    def test_search_prefix_returns_matches(self):
        results = self.tree.search_prefix("b")
        titles = [r.title for r in results]
        self.assertIn("Banana Bread", titles)

    def test_search_prefix_no_matches(self):
        results = self.tree.search_prefix("xyz")
        self.assertEqual(results, [])

    #in order traversal

    def test_inorder_is_alphabetical(self):
        recipes = self.tree.inorder()
        titles = [r.title for r in recipes]
        self.assertEqual(titles, sorted(titles, key=lambda t: t.lower()))

    #AVL balance

    def test_tree_height_is_logarithmic(self):
        #with 5 nodes a balanced tree should never exceed height 4
        self.assertLessEqual(self.tree.get_height(), 4)

    def test_large_insert_stays_balanced(self):
        #insert 100 recipes in alphabetical order
        tree = AVLTree()
        for i in range(100):
            tree.insert(f"Recipe {i:03}", ["ingredient"], "instructions")
        #a plain BST would hit height 100 AVL should stay around log2(100) = 7
        self.assertLessEqual(tree.get_height(), 14)


if __name__ == "__main__":
    unittest.main()