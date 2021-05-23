'''
def dfs(maps, x, y, count, result):
    print(x, y, count)
    if x == len(maps) - 1 and y == len(maps[0]) - 1:
        result.append(count)

    if x <= -1 or x >= len(maps) or y <= -1 or y >= len(maps[0]):
        return
    if maps[x][y] == 1:
        maps[x][y] = 0
        dfs(maps, x-1, y, count+1, result)
        dfs(maps, x, y-1, count+1, result)
        dfs(maps, x+1, y, count+1, result)
        dfs(maps, x, y+1, count+1, result)
        maps[x][y] = 1
        return
    return


def solution(maps):
    answer = 0
    cnt = 1
    result = []
    dfs(maps, 0, 0, cnt, result)
    if result:
        answer = min(result)
    else:
        answer = -1
    return answer
'''
# 위의 풀이는 효율성 망

from collections import deque


def solution(maps):
    return bfs(maps)


def bfs(maps):
    dy, dx = [1,-1,0,0], [0,0,1,-1]
    dist = [[-1] * len(maps[0]) for _ in range(len(maps))]
    dist[0][0] = 1
    q = deque([(0, 0)])
    while q:
        cy, cx = q.popleft()
        for d in range(4):
            ny, nx = cy + dy[d], cx + dx[d]
            if 0 <= ny < len(maps) and 0 <= nx < len(maps[0]):
                if dist[ny][nx] == -1 and maps[ny][nx] == 1:
                    dist[ny][nx] = dist[cy][cx] + 1
                    q.append((ny, nx))
    return dist[-1][-1]

maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]

print(solution(maps))