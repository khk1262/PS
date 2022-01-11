'''
dfs를 생각하는게 가장 큰 핵심

이때 dfs의 키포인트라 할 수 있는 맨 밑으로 파고들어가서 결과에 도달하면 거기서부터 값을 return 한다는 것을 생각해야한다.
현재 문제에 적용한다면, 가장 도착점 가까이에서부터 경로를 되짚어나가 만약 경로가 여러갈래로 뻗어나갈 수 있는 부분은 해당 경로들이 다 더해진 구간으로 표시되며,
이러한 식으로 계속 출발점까지 거슬러 올라간다.
'''
m, n = map(int, input().split())
graph = []
visited = [[-1] * n for _ in range(m)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def dfs(x, y):
    if x == m-1 and y == n-1:
        return 1
    if visited[x][y] != -1:
        return visited[x][y]

    visited[x][y] = 0
    for i in range(4):
        if 0 <= x+dx[i] < m and 0 <= y + dy[i] < n:
            if graph[x][y] > graph[x+dx[i]][y+dy[i]]:
                visited[x][y] += dfs(x+dx[i], y+dy[i])
    return visited[x][y]


for _ in range(m):
    graph.append(list(map(int, input().split())))

print(dfs(0, 0))