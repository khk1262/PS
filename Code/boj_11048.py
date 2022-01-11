dx = [1, 0, 1]
dy = [0, 1, 1]

n, m = map(int, input().split())
graph = []

for _ in range(n):
    graph.append(list(map(int, input().split())))

visited = [[0] * m for _ in range(n)]
visited[0][0] = graph[0][0]
for i in range(n):
    for j in range(m):
        for k in range(3):
            if i+dx[k] < n and j+dy[k] < m:
                visited[i+dx[k]][j+dy[k]] = max(visited[i+dx[k]][j+dy[k]], visited[i][j] + graph[i+dx[k]][j+dy[k]])

print(visited[n-1][m-1])