A, B, C, N = map(int, input().split())
result = 0

# for i in range(N):
#     for j in range(N):
#         for k in range(N):
#             if (A*i + B*j + C*k) == N:
#                 result = 1
#
# print(result)

# 문제인식, 현재의 값이 배정된 방들의 합으로 표현이 되면 나누어 떨어지는 것이 아닌가?
# 처음부터 시작해서 더해간다.
# A, B, C에는 미리 1을 넣어기에 dp[i] 조건을 통해 넘어가진다

dp = [0 for _ in range(301)]
dp[A] = dp[B] = dp[C] = 1

for i in range(N+1):
    dp[i] = 1 if dp[i] or dp[i-A] or dp[i-B] or dp[i-C] else 0

print(dp[N])