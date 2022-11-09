from tree import BSTree
from treebalancer import treebal

class sortedset:
    def __init__(self, initialvalue = None):
        self.tree = BSTree(headvalue=initialvalue)
    
    def add(self, value):
        """Adds the given value to the set, if it is new

        Args:
            value (any): the value to be added
        """
        try:
            self.tree.add(value)
        except Exception:
            pass

    def rephelper(self, pointer)->str:
        """Helps the __repr__ create a string

        Args:
            pointer (any): initially the head node of the tree, becomes the node that is currently being converted

        Returns:
            str: a string containing the data in the set
        """
        rep = ""
        spacer = " "
        if pointer is not None:
            if pointer.data is not None:
                rep += self.rephelper(pointer.left)
                rep += spacer
                rep += str(pointer.data)
                rep += spacer
                rep += self.rephelper(pointer.right)
        return rep

    def contains(self, value)->bool:
        """Checks if a given value is inside of the set

        Args:
            value (_type_): the value that is being checked for

        Returns:
            bool: True if the value is in the set, False if not
        """
        return self.tree._search(value)
    
    def rebaltree(self):
        """Rebalances the tree
            Uses the tree balancer
            Should be called when adding to the set is completed, or when adding a chunk is completed.
        """
        self.tree = treebal.balance(self.tree)

    def __repr__(self)->str:
        return str(self.rephelper(self.tree.headnode))
