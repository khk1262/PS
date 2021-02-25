import sys, math

input = sys.stdin.readline
divid = int(1e9) + 7


def init(node, start, end):
    if start == end:
        tree[node] = li[start]
        return tree[node]

    tree[node] = (init(2*node, start, (start + end) // 2) * init(2*node+1, (start + end) // 2 + 1, end)) % divid
    return tree[node]


def mul(node, start, end, left, right):
    if left > end or right < start:
        return 1
    if left <= start and end <= right:
        return tree[node]
    return (mul(2*node, start, (start + end) // 2, left, right) * mul(2*node + 1, (start + end) // 2 + 1, end, left, right)) % divid


def update(node, start, end, index, num):
    if index < start or end < index:
        return tree[node]

    if start == end:
        tree[node] = num
        return tree[node]

    tree[node] = (update(2*node, start, (start + end) // 2, index, num) * update(2*node + 1, (start + end) // 2 + 1, end, index, num)) % divid
    return tree[node]


N, M, K = map(int, input().split())

height = 1 << (math.ceil(math.log2(N)) + 1)
tree = [1] * height

li = [int(input()) for _ in range(N)]

init(1, 0, N-1)

for _ in range(M+K):
    a, b, c = map(int, input().split())

    if a == 1:
        update(1, 0, N-1, b-1, c)
    else:
        print(mul(1, 0, N-1, b-1, c-1)%divid)
