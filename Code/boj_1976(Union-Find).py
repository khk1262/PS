import sys
input = sys.stdin.readline

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

N = int(input())
M = int(input())

p = [i for i in range(N+1)]

for i in range(1, N+1):
    temp = list(map(int, input().split()))
    for j in range(len(temp)):
        if temp[j] == 1:
            if not check(i, j+1):
                merge(i, j+1)

tour = list(map(int, input().split()))
can_tour = True

for i in range(1, len(tour)):
    can_tour *= check(p[tour[0]], p[tour[i]])

print("YES") if can_tour else print("NO")


