class RecipeNode:
    """
    Single node in AVL tree
    
    Each node stores a recipes title as the ket which is used for the ordering and balancing
    and it also has the full recipes data with the ingreditents and instructions to make
    
    """

    def __init__(self, title: str, ingredients: list, instructions: str = ""):
        #this is recipe data
        self.title = title
        self.ingredients = ingredients
        self.instructions = instructions
        #new nodes start at 1
        self.height = 1
        self.left = None
        self.right = None