from kvnode import node
class tree:
    def __init__(self, headkey = None, headvalue = None):
        self.head = node(headkey, headvalue)

    def add(self, key:str, value:int):
        if self.head.getKey() is None:
            self.head.setKey(key)
            self.head.setValue(value)
        self._add(self.head, node(key, value))
        
    def _add(self, oldnode, newnode):
        if newnode.getKey()<oldnode.getKey():
            if oldnode.getLeft() is None:
                oldnode.setLeft(newnode)
            else:
                self._add(oldnode.getLeft(), newnode)
        elif newnode.getKey()>oldnode.getKey():
            if oldnode.getRight() is None:
                oldnode.setRight(newnode)
            else:
                self._add(oldnode.getRight(), newnode)

    def find(self, key:str)->int:
        if self.head is None:
            return None
        if self.head.getKey() == key:
            return self.head.value
        return self._search(self.head, key)

    def _search(self, currnode:node, lookKey:str)->int:
        if currnode.getKey()<lookKey:
            return self._search(currnode.getRight(), lookKey)
        elif currnode.getKey()>lookKey:
            return self._search(currnode.getLeft(), lookKey)
        else:
            return currnode.getValue()

    def __repr__(self):
        return str(self.head)

