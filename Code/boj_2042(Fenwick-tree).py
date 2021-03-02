import sys, math

input = sys.stdin.readline


def update_node(tree, i, diff):
    while i < len(tree):
        tree[i] += diff
        i += (i & -i)


def sum_node(tree, i):
    ans = 0
    while i > 0:
        ans += tree[i]
        i -= (i & -i)
    return ans


if __name__ == '__main__':
    N, M, K = map(int, input().split())
    li = [0] * (N+1)
    tree = [0] * (N+1)

    for i in range(1, N + 1):
        li[i] = int(input())
        update_node(tree, i, li[i])

    for _ in range(M+K):
        a, b, c = map(int, input().split())

        if a == 1:
            diff = c - li[b]
            li[b] = c
            update_node(tree, b, diff)
        else:
            print(sum_node(tree, c) - sum_node(tree, b-1))
