from node import Node
class tree:
    def __init__(self, headnode:Node = None, headvalue = None):
        if headnode is not None:
            self.headnode = headnode
        else:
            self.headnode = Node(headvalue)
    
    def _add(self, addvalue):
        if self.headnode is None:
            self.headnode.data = addvalue
        else:
            self._addhelper(self.head, addvalue)
        
    def _addhelper(self, pointernode:Node, newdata):
        if newdata < pointernode.data:
            if pointernode.left is None:
                pointernode.left = Node(value=newdata)
            else:
                self._addhelper(pointernode.left, newdata)
        elif newdata > pointernode.data:
            if pointernode.right is None:
                pointernode.right = Node(newdata)
            else:
                self._addhelper(pointernode.right, newdata)
    
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
        if pointernode.data < value:
            return self._searchhelper(pointernode.right, value)
        elif pointernode.data > value:
            return self._searchhelper(pointernode.left, value)
        elif pointernode.data == value:
            return True
        else:
            return False

    def __repr__(self)->str:
        return str(self.headnode)