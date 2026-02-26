class AVLTree:
    """
    Self balancing binary search tree (AVL) that is keyed by recipe title
    
    It makes sure it is O(logn) time for the insert, search and delete (add more later)"""

    def __init__(self):
        self.root = None
        self._size = 0