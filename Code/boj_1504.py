import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

N, E = map(int, input().split())

graph = [[] for _ in range(N+1)]

for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

v1, v2 = map(int, input().split())


def dijkstra(s):
    hq = []
    distance = [INF for _ in range(N + 1)]

    distance[s] = 0
    heapq.heappush(hq, (0, s))

    while hq:
        dist, node = heapq.heappop(hq)
        if distance[node] < dist:
            continue
        for next in graph[node]:
            cost = next[1] + dist
            if distance[next[0]] > cost:
                distance[next[0]] = cost
                heapq.heappush(hq, (cost, next[0]))
    return distance


li1 = dijkstra(1)
li_v1 = dijkstra(v1)
li_v2 = dijkstra(v2)

result = min(li1[v1] + li_v1[v2] + li_v2[N], li1[v2] + li_v2[v1] + li_v1[N])
print(result) if result < INF else print(-1)