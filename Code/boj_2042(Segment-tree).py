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


def update_node(node, start, end, index, diff):
    if index < start or index > end:
        return
    tree[node] += diff
    if start != end:
        update_node(2*node, start, (start + end) // 2, index, diff)
        update_node(2*node + 1, (start + end) // 2 + 1, end, index, diff)


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
        diff = c - li[b-1]
        li[b-1] = c
        update_node(1, 0, N-1, b-1, diff)
    else:
        print(sum_node(1, 0, N-1, b-1, c-1))

    M -= 1
