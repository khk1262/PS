import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)


def dijkstra(start):
    distance = [INF] * (V + 1)
    distance[start] = 0
    hq = []
    heapq.heappush(hq, (distance[start], start))

    while hq:
        cur_dis, cur_node = heapq.heappop(hq)
        if distance[cur_node] < cur_dis:
            continue
        for new_node, new_dis in graph[cur_node]:
            dist = cur_dis + new_dis
            if dist < distance[new_node]:
                distance[new_node] = dist
                heapq.heappush(hq, (dist, new_node))
    return distance


V, E = map(int, input().split())
K = int(input())

graph = [[] for _ in range(V+1)]

for i in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

li = dijkstra(K)

for i in range(1, V+1):
    print(li[i]) if li[i] != INF else print('INF')
