import sys
import heapq

input = sys.stdin.readline
inf = int(1e9)

n = int(input())
graph = [[] for _ in range(n+1)]


for _ in range(n-1):
    a, b, c = map(int, input().split())
    graph[a].append([b,c])
    graph[b].append([a,c])


def dijkstra(start, mode):
    hq = []
    distance = [inf for _ in range(n+1)]
    distance[start] = 0

    heapq.heappush(hq, (0, start))

    while hq:
        dist, node = heapq.heappop(hq)
        if dist > distance[node]:
            continue
        for next in graph[node]:
            cost = dist + next[1]

            if cost < distance[next[0]]:
                distance[next[0]] = cost
                heapq.heappush(hq, (cost, next[0]))

    if mode == 1:
        return distance.index(max(distance[1:]))
    else:
        return max(distance[1:])


print(dijkstra(dijkstra(1,1),2))