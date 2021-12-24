# import sys
#
# input = sys.stdin.readline
# inf = int(1e9)
#
# n, k = map(int, input().split())
#
# dp = [[inf] * (k+1) for _ in range(n+1)]
# cost = [0] * n
#
# for i in range(n):
#     cost[i] = int(input())
#
# for i in range(n):
#     dp[i][0] = 0
#     for j in range(k+1):
#         dp[i+1][j] = min(dp[i+1][j], dp[i][j])
#         jj = j + cost[i]
#         if jj <= k:
#             dp[i][jj] = min(dp[i][jj], dp[i][j] + 1)
#
# print(dp[n-1][k] if dp[n-1][k] != inf else -1)

n, k = map(int, input().strip().split())

coin = [0] * 101
dp = [0] + [100001] * 100000

for i in range(1, n+1):
    coin[i] = int(input())
    for j in range(coin[i], k+1):
        dp[j] = min(dp[j-coin[i]] + 1, dp[j])
        print(dp[:k+1])
if dp[k] == 100001:
    print(-1)
else:
    print(dp[k])

print(dp[:k+1])