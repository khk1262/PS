import sys
import heapq

input = sys.stdin.readline
inf = int(1e9)

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

M, N = map(int, input().split())
graph = []

for _ in range(N):
    graph.append(list(map(int, list(input().strip()))))


def dijkstra():
    dis = [[inf] * M for _ in range(N)]
    visited = [[0] * M for _ in range(N)]
    hq = []

    dis[0][0] = 0
    visited[0][0] = 1

    heapq.heappush(hq, (0, 0, 0))

    while hq:
        cost, a, b = heapq.heappop(hq)

        if a == N - 1 and b == M - 1:
            print(cost)
            return

        for i in range(4):
            x = a + dx[i]
            y = b + dy[i]

            if 0 <= x < N and 0 <= y < M and visited[x][y] == 0:
                heapq.heappush(hq, (cost+1 if graph[x][y] == 1 else cost, x, y))
                visited[x][y] = 1


dijkstra()