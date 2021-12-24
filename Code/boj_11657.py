import sys

input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    dp = [[0] * 3 for _ in range(n+1)]
    li = []
    for _ in range(2):
        temp = list(map(int, input().split()))
        li.append(temp)
    for i in range(n):
        dp[i + 1][0] = max(dp[i])
        dp[i + 1][1] = max(dp[i][0], dp[i][2]) + li[0][i]
        dp[i + 1][2] = max(dp[i][0], dp[i][1]) + li[1][i]
    print(max(dp[n]))