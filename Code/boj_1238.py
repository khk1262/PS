import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

N, M, X = map(int, input().split())

graph = [[] for _ in range(M+1)]

for _ in range(M):
    a, b, c = map(int,input().split())
    graph[a].append((b, c))


def dijkstra(start):
    distance = [INF for _ in range(N + 1)]
    hq = []

    distance[start] = 0
    heapq.heappush(hq, (0, start))

    while hq:
        dist, node = heapq.heappop(hq)

        if dist > distance[node]:
            continue
        for next in graph[node]:
            cost = dist + next[1]
            if distance[next[0]] > cost:
                distance[next[0]] = cost
                heapq.heappush(hq, (cost, next[0]))

    return distance


max_v = -1
li_e = dijkstra(X)

for i in range(1, N+1):
    li_s = dijkstra(i)
    max_v = max(max_v, li_s[X] + li_e[i])

print(max_v)