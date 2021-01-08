dp = [1, 0]

N = int(input())

for _ in range(N):
    temp = [0, 0]
    if dp[0] > 0:
        temp[1] += dp[0]
        dp[0] = 0
    temp[1] += dp[1]
    temp[0] += dp[1]
    dp = temp[:]

print(*dp)
