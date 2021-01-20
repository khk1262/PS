# Trie를 활용하여 푼 문제, 트라이 자료구조를 반드시 숙지

import sys

class Node(object):
    """
    A node that consists of trie.
    """
    def __init__(self, key):
        self.key = key
        self.data = None
        self.children = {}
        self.child = False


class Trie(object):
    def __init__(self):
        self.head = Node(None)

    """
    insert string to Trie
    """
    def insert(self, string):
        curr_node = self.head

        for char in string:
            if char not in curr_node.children:
                curr_node.children[char] = Node(char)
                curr_node.child = True

            curr_node = curr_node.children[char]

        curr_node.data = string

    """
    return exist string in Trie
    """

    def search(self, string):
        curr_node = self.head

        for char in string:
            if char in curr_node.children:
                curr_node = curr_node.children[char]
            else:
                return False

        if curr_node.data is not None:
            return True

    # 일관성 검사의 경우 dfs 방식을 통해 검사하였음
    def consistent(self):
        curr_node = self.head

        stack = list(curr_node.children.values())

        while stack:
            temp_node = stack.pop()

            if temp_node.data is not None and temp_node.child:
                return False

            stack += list(temp_node.children.values())

        return True


'''
Python을 사용하고 있다면, input 대신 sys.stdin.readline을 사용할 수 있다.
 단, 이때는 맨 끝의 개행문자까지 같이 입력받기 때문에 문자열을 저장하고 싶을 경우
.rstrip()을 추가로 해 주는 것이 좋다
'''

for _ in range(int(sys.stdin.readline())):
    trie = Trie()
    for _ in range(int(sys.stdin.readline())):
        phone = sys.stdin.readline().strip()
        trie.insert(phone)

    print("YES") if trie.consistent() else print("NO")