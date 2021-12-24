import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)
N = int(input())
M = int(input())

graph = [[] for _ in range(N+1)]
distance = [INF for _ in range(N + 1)]

for i in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

s, e = map(int, input().split())

def dijkstra(start):
    hq = []

    distance[start] = 0
    heapq.heappush(hq, (0, start))

    while hq:
        dist, node = heapq.heappop(hq)

        if distance[node] < dist:
            continue

        for next in graph[node]:
            cost = dist + next[1]

            if distance[next[0]] > cost:
                distance[next[0]] = cost
                heapq.heappush(hq, (cost, next[0]))


dijkstra(s)
print(distance[e])