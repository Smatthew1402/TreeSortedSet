class Node:
    def __init__(self, value, left = None, right = None):
        self.data = value
        self.left = left
        self.right = right
    
    def __repr__(self):
        rep = "("
        rep += str(self.data)
        if self.left is not None:
            rep += str(self.left)
        if self.right is not None:
            rep += str(self.right)
        rep += ")"
        return rep