import sys
import math

input = sys.stdin.readline


def init(node, start, end):
    if start == end:
        tree[node] = li[start]
        return tree[node]
    else:
        tree[node] = init(2*node, start, (start + end) // 2) + init(2*node + 1, (start + end) // 2 + 1, end)
        return tree[node]


def sum_node(node, start, end, left, right):
    if start > right or end < left:
        return 0
    if start >= left and end <= right:
        return tree[node]
    return (sum_node(2*node, start, (start + end) // 2, left, right) + sum_node(2*node + 1, (start + end) // 2 + 1, end, left, right))


def update_node(node, start, end, index, k):
    if index < start or index > end:
        return tree[node]
    if start == end:
        tree[node] = k
        return tree[node]
    tree[node] = update_node(2*node, start, (start + end) // 2, index, k) + update_node(2*node + 1, (start + end) // 2 + 1, end, index, k)
    return tree[node]

N, M, K = map(int, input().split())

li = [0] * N
M += K
tree_height = (1 << (math.ceil(math.log2(N)) + 1))
tree = [0] * tree_height

for i in range(N):
    li[i] = int(input())

init(1, 0, N-1)

while M:
    a, b, c = map(int, input().split())

    if a == 1:
        update_node(1, 0, N-1, b-1, c)
    else:
        print(sum_node(1, 0, N-1, b-1, c-1))

    M -= 1

# import sys
# import math
#
# input = sys.stdin.readline
#
#
# def init():
#     tree[size:size+N] = li[:]
#     for i in range(size-1, 0, -1):
#         tree[i] = tree[i*2] + tree[i*2+1]
#
#
# def sum_node(node, start, end, left, right):
#     if start > right or end < left:
#         return 0
#     if start >= left and end <= right:
#         return tree[node]
#     return sum_node(2*node, start, (start + end) // 2, left, right) + sum_node(2*node + 1, (start + end) // 2 + 1, end, left, right)
#
#
# def update_node(index, k):
#     index += size
#     tree[index] = k
#     while index:
#         index //= 2
#         tree[index] = tree[index*2] + tree[index*2+1]
#
#
# N, M, K = map(int, input().split())
#
# li = [0] * N
# M += K
# tree_height = (1 << (math.ceil(math.log2(N)) + 1))
# tree = [0] * tree_height
# size = tree_height >> 1
#
# for i in range(N):
#     li[i] = int(input())
#
# init()
#
# while M:
#     a, b, c = map(int, input().split())
#     print(tree)
#     if a == 1:
#         update_node(b-1, c)
#     else:
#         print(sum_node(1, 0, N-1, b-1, c-1))
#     M -= 1
#
