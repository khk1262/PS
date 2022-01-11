dp = [1] * 1001

n = int(input())
li = list(map(int, input().split()))

for i in range(n):
    for j in range(i):
        if li[i] > li[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(dp[n-1])