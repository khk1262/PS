n = int(input())
w = [list(map(int, input().split())) for _ in range(n)]
inf = int(1e9)
visited = [0 for _ in range(n)]


def tsp(node, cntSum, total):
    if total == n:
        if w[node][0] != 0:
            return cntSum + w[node][0]
        return inf
    visited[node] = True
    ret = inf
    for i in range(n):
        if not visited[i] and w[node][i] != 0:
            ret = min(ret, tsp(i, cntSum+w[node][i], total+1))
    visited[node] = False

    return ret

print(tsp(0, 0, 1))