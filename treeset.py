from tree import BSTree

class sortedset:
    def __init__(self, initialvalue = None):
        self.tree = BSTree(headvalue=initialvalue)
    
    def add(self, value):
        try:
            self.tree.add(value)
        except Exception:
            pass

    def rephelper(self, pointer)->str:
        rep = ""
        spacer = " "
        if pointer.value is not None:
            rep += self.rephelper(pointer.left)
            rep += spacer
            rep += str(pointer.data)
            rep += spacer
            rep += self.rephelper(pointer.right)
            
    
    def __repr__(self)->str:
        return self.rephelper(self.tree.headnode)
