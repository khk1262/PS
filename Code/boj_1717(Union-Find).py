import sys

input = sys.stdin.readline

n, m = map(int, input().split())

p = [i for i in range(n+1)]


def find(a):
    if a == p[a]:
        return a
    p[a] = find(p[a])
    return p[a]


def merge(a, b):
    a = find(a)
    b = find(b)
    if a == b:
        return
    p[b] = a


def check(a, b):
    a = find(a)
    b = find(b)
    if a == b:
        return True
    else:
        return False


for i in range(m):
    command, A, B = map(int, input().split())
    if not command:
        merge(A, B)
    else:
        print("YES") if check(A, B) else print("NO")