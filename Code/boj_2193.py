n = int(input())

dp = [[0] * 2 for _ in range(91)]

dp[1][1] = 1
dp[2][0] = 1
dp[3][0] = 1
dp[3][1] = 1

for i in range(4, n+1):
    dp[i][0] = dp[i-1][0] + dp[i-1][1]
    dp[i][1] = dp[i-1][0]

print(dp[n][0] + dp[n][1])