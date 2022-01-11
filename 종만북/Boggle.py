dx = [-1, -1, -1, 1, 1, 1, 0, 0]
dy = [-1, 0, 1, -1, 0, 1, -1, 1]


def isin(y, x):
    if 0 <= x < 5 and 0 <= y < 5:
        return True
    else:
        return False


def hasword(y, x, word):
    if not isin(y, x):
        return False
    if graph[y][x] != word[0]:
        return False
    if len(word) == 1:
        return True

    for i in range(8):
        nexty = y + dy[i]
        nextx = x + dx[i]

        if hasword(nexty, nextx, word[1:]):
            return True
    return False


t = int(input())
for _ in range(t):
    graph = [list(input()) for _ in range(5)]
    n = int(input())
    words = [list(input()) for _ in range(n)]
    for w in words:
        check = 0
        for i in range(5):
            for j in range(5):
                if hasword(i, j, w):
                    check += 1
        if check:
            print(''.join(w), "YES")
        else:
            print(''.join(w), "NO")
