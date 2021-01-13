N = int(input())
li = list(map(int, input().split()))

dp = li[:]
result = -1
for i in range(N):
    for j in range(i):
        if (li[j] < li[i]) and (dp[i] < dp[j] + li[i]):
            dp[i] = dp[j] + li[i]
    result = max(result, dp[i])

print(result)

'''
dp 배열을 통해 이미 이전 증가 부분 수열의 합을 구해 놓은 상황에서 현재 인덱스의 값을 더해나감으로써 이를 이어나간다.

즉 점화식을 보게되면 
i < j
입력받은 수열 중 a[i] < a[j] 이고, 현재 구하는 합 dp[i]이 이전번째까지의 합 dp[j] + 자기자신 값 li[i]보다 작으면,
dp[i] = dp[j] + a[i] 임

'''