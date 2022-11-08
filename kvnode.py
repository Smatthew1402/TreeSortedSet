class node:
    def __init__(self, keyin:str = None, valuein:int = None,  leftin = None, rightin = None):
        self.key = keyin
        self.value = valuein
        self.left = leftin
        self.right = rightin
    
    def getRight(self):
        return self.right

    def setRight(self, rightin):
        self.right = rightin
    
    def getLeft(self):
        return self.left

    def setLeft(self, leftin):
        self.left = leftin

    def getKey(self)->str:
        return self.key

    def setKey(self, key:str):
        self.key = key

    def getValue(self)->int:
        return self.value
    
    def setValue(self, val:int):
        self.value = val
    
    
    def __repr__(self):
        return "(" + str(self.key) + ":" + str(self.value) + " " + str(self.left) + " " + str(self.right) + ")"
