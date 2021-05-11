import sys, math
INF = int(1e9)
input = sys.stdin.readline


def update_min_node(tree, arr, index, num, node, start, end):
    if index < start or index > end:
        return tree[node]
    if start == end:
        tree[node] = num
        return tree[node]

    tree[node] = min(update_min_node(tree, arr, index, num, 2 * node, start, (start + end) // 2),
                     update_min_node(tree, arr, index, num, 2 * node + 1, (start + end) // 2 + 1, end))
    return tree[node]


def find_min(tree, node, start, end, left, right):
    if right < start or left > end:
        return INF
    if left <= start and end <= right:
        return tree[node]

    return min(find_min(tree, 2 * node, start, (start + end) // 2, left, right),
               find_min(tree, 2 * node + 1, (start + end) // 2 + 1, end, left, right))


N, M = map(int, input().split())
height = 1 << (math.ceil(math.log2(N)) + 1)
min_tree = [INF] * height
li = [0] * N

for i in range(N):
    li[i] = int(input())
    update_min_node(min_tree, li, i, li[i], 1, 0, N-1)

for j in range(M):
    a, b = map(int, input().split())
    print(find_min(min_tree, 1, 0, N - 1, a - 1, b - 1))
