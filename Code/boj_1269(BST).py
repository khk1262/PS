# BST 자료구조를 활용한 풀이 매우 김

class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


class BST(object):
    def __init__(self):
        self.root = None

    def insert(self, data):
        self.root = self._insert(self.root, data)
        return self.root is not None

    def _insert(self, node, data):
        if node is None:
            node = Node(data)
        else:
            if data > node.data:
                node.right = self._insert(node.right, data)
            else:
                node.left = self._insert(node.left, data)
        return node

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        if node is None or node.data == key:
            return node is not None

        if key > node.data:
            return self._search(node.right, key)
        else:
            return self._search(node.left, key)


N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
bst = BST()
union = []


for i in A:
    bst.insert(i)

for j in B:
    if bst.search(j):
        union.append(j)

print(len(A) + len(B) - 2 * len(union))


##단순 set
# N, M = map(int, input().split())
# A = set(map(int, input().split()))
# B = set(map(int, input().split()))
#
# print(len(A-B) + len(B-A))