class Node(object):
    def __init__(self, data):
        self.data = data
        self.right = self.left = None

class BTS(object):
    def __init__(self):
        self.root = None

    def insert(self, data):
        self.root = self._insert(self.root, data)
        return self.root is not None

    def _insert(self, node, data):
        if node is None:
            node = Node(data)

        else:
            if node.data >= data:
                node.left = self._insert(node.left, data)
            else:
                node.right = self._insert(node.right, data)

        return node

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        if node is None or node.data == key:
            return node is not None

        elif key < node.data:
            return self._search(node.left, key)
        else:
            return self._search(node.right, key)

    def delete(self, key):
        node, delete = self._delete(self.root, key)
        return delete

    def _delete(self, node, key):
        if node is None:
            return node, False

        if key == node.data:
            delete = True
            if node.right and node.left:
                parent, child = node, node.right

                while child.left is not None:
                    parent, child = child, child.left

                child.left = node.left

                if parent != node:
                    parent.left = child.right
                    child.right = node.right

                node = child

            elif node.right or node.left:
                node = node.right or node.left

        elif key < node.data:
            node.left, delete = self._delete(node.left, key)

        else:
            node.right, delete = self._delete(node.right, key)

        return node, delete

    def pre_order(self):
        def _pre_order(node):
            if node is None:
                return
            else:
                print(node.data)
                _pre_order(node.left)
                _pre_order(node.right)
        _pre_order(self.root)


array = [40, 4, 34, 45, 14, 55, 48, 13, 15, 49, 47]

bst = BTS()
for x in array:
    bst.insert(x)

bst.pre_order()