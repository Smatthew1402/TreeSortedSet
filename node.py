class Node:
    def __init__(self, value, left = None, right = None, parent = None):
        self.data = value
        self.left = left
        self.right = right
        self.parent = parent
    
    def __repr__(self):
        return "(" + str(self.data) + " " + str(self.left) + " " + str(self.right) + ")"