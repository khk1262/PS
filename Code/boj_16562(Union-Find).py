import sys

input = sys.stdin.readline

N, M, K = map(int, input().split())

money = [0] + list(map(int, input().split()))

p = [-1 for i in range(N+1)]


def find(a):
    if p[a] < 0:
        return a
    p[a] = find(p[a])
    return p[a]


def merge(a, b):
    a = find(a)
    b = find(b)
    if a == b:
        return
    if money[a] < money[b]:
        p[b] = a
    else:
        p[a] = b


for i in range(M):
    t1, t2 = map(int, input().split())
    merge(t1, t2)

result = 0

for i in range(1, len(p)):
    if p[i] == -1:
        result += money[i]

print(result) if result <= K else print("Oh no")
