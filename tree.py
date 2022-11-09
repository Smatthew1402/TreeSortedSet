from node import Node
class BSTree:
    def __init__(self, headvalue = None):
        if headvalue is not None:
            self.headnode = Node(value = headvalue)
            self.count = 1
        else:
            self.headnode = None
            self.count = 0

    
    def _add(self, addvalue):
        if self.headnode is None:
            self.headnode = Node(addvalue)
        else:
            self._addhelper(self.headnode, addvalue)
        self.count +=1
        
    def _addhelper(self, pointernode:Node, newdata):
        if newdata < pointernode.data:
            if pointernode.left is None:
                pointernode.left = Node(value=newdata)
            else:
                self._addhelper(pointernode.left, newdata)
        elif newdata > pointernode.data:
            if pointernode.right is None:
                pointernode.right = Node(value=newdata)
            else:
                self._addhelper(pointernode.right, newdata)
        elif newdata == pointernode.data:
            raise Exception
    
    def add(self, newvalue):
        self._add(newvalue)

    def _search(self, value)->bool:
        if self.headnode is None:
            return False
        if self.headnode.data == value:
            return True
        else:
            return self._searchhelper(self.headnode, value)

    def _searchhelper(self, pointernode:Node, value)->bool:
        if pointernode is not None:
            if pointernode.data == value:
                return True
            if pointernode.left is None and pointernode.right is None:
                return False
            if pointernode.left is not None:
                if pointernode.data > value:
                    return self._searchhelper(pointernode.left, value)
            if pointernode.right is not None:
                if pointernode.data < value:
                    return self._searchhelper(pointernode.right, value)
        else:
            return False

    def __repr__(self)->str:
        return str(self.headnode)