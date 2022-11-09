class Node:
    def __init__(self, value, left:Node = None, right:Node = None):
        self.data = value
        self.left = left
        self.right = right
    
    def __repr__(self):
        return "(" + str(self.data) + " " + str(self.left) + " " + str(self.right) + ")"