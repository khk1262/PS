import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
start = int(input())

graph = [[] for i in range(n + 1)]
visited = [False] * (n+1)
distance = [INF] * (n+1)
heap = []

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c)) #이어진 정점 번호, 거리


def dijkstra(start):
    distance[start] = 0
    heapq.heappush(heap, (0, start))

    while heap:
        while True:
            curr = heapq.heappop(heap)[1]
            if not heap or visited[curr] is False: # heap이 비거나 방문한 정점이 아닐 경우 빠져나옴
                break
        if visited[curr]: # heap이 비어서 끝났을 경우의 방문 정점 확인
            break
        visited[curr] = True
        for node in graph[curr]:
            next, dist = node
            if distance[next] > distance[curr] + dist:
                distance[next] = distance[curr] + dist
                heapq.heappush(heap, (distance[next], next))


dijkstra(start)

for i in range(1, len(distance)):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])


'''
밑의 코드로 해도 문제는 없음
차이는 방문여부를 체크하냐 안하냐 차이
'''

# import sys
# import heapq
#
# input = sys.stdin.readline
# INF = int(1e9)
#
# n, m = map(int, input().split())
# start = int(input())
#
# graph = [[] for i in range(n + 1)]
# distance = [INF] * (n+1)
# heap = []
#
# for _ in range(m):
#     a, b, c = map(int, input().split())
#     graph[a].append((b, c)) #이어진 정점 번호, 거리
#
#
# def dijkstra(start):
#     distance[start] = 0
#     heapq.heappush(heap, (0, start))
#
#     while heap:
#         curr = heapq.heappop(heap)[1]
#         for node in graph[curr]:
#             next, dist = node
#             if distance[next] > distance[curr] + dist:
#                 distance[next] = distance[curr] + dist
#                 heapq.heappush(heap, (distance[next], next))
#
#
# dijkstra(start)
#
# for i in range(1, len(distance)):
#     if distance[i] == INF:
#         print("INF")
#     else:
#         print(distance[i])
