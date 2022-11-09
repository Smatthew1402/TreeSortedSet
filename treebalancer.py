from tree import BSTree
class treebal:

    def balance(tree:BSTree)->BSTree:
        datalist = treebal.makelist(tree)
        return treebal._balancehelper(datalist)

    def _balancehelper(listin, newtree:BSTree = BSTree(), min=0, max=None)->BSTree:
        if max is None:
            max = len(listin)-1
        mid = min + int((max-min)/2)
        try:
            newtree.add(listin[mid])
        except Exception:
            pass
        if max-min >0:
            treebal._balancehelper(listin, newtree, mid+1, max)
            treebal._balancehelper(listin, newtree, min, mid-1)
        if newtree.count == len(listin):
            return newtree


    def makelist(tree)->list:
        return treebal._listhelper(tree.headnode)

    def _listhelper(pointer, datalist =[]):
        if pointer is not None:
            if pointer.data is not None:
                treebal._listhelper(pointer.left, datalist)
                datalist.append(pointer.data)
                treebal._listhelper(pointer.right, datalist)
        return datalist
    
