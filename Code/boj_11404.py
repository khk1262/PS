import sys

input = sys.stdin.readline
inf = int(1e9)
n = int(input())
m = int(input())

graph = [[inf if i != j else 0 for i in range(n+1)] for j in range(n+1)]

for i in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = min(graph[a][b], c)


def floyd():
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                cost = graph[i][k] + graph[k][j]
                if cost < graph[i][j]:
                    graph[i][j] = cost


floyd()

for line in graph[1:]:
    for t in line[1:]:
        print(t if t != inf else 0, end=' ')
    print()