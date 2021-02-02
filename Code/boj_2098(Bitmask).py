def tsp(current, visit):
    if visit == total:
        return W[current][0] if W[current][0] != 0 else 1e9
    if dp[current][visit] != 0:
        return dp[current][visit]

    dp[current][visit] = 1e9
    for i in range(N):
        next = 1 << i
        if W[current][i] == 0 or (visit & next) != 0:
            continue
        dp[current][visit] = min(dp[current][visit], tsp(i, visit | next) + W[current][i])
    return dp[current][visit]


N = int(input())
W = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * (1<<N) for _ in range(N)]
total = (1<<N) - 1
print(tsp(0, 1))