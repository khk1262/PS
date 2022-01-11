n = int(input())

dp = [0] * (1000001)
dp[2] = dp[3] = 1

li = [[i] for i in range(1000001)]
li[1] = [1]
li[2] = [1, 2]
li[3] = [1, 3]

for i in range(4, n+1):
    dp[i] = dp[i-1] + 1
    temp = li[i-1]
    if not i % 2:
        if dp[i] > dp[i//2] + 1:
            dp[i] = dp[i//2] + 1
            temp = li[i//2]

    if not i % 3:
        if dp[i] > dp[i//3] + 1:
            dp[i] = dp[i//3] + 1
            temp = li[i//3]

    li[i] += temp

print(dp[n])
print(*(sorted(li[n], reverse=True)))