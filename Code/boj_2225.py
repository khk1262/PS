n, k = map(int, input().split())
dp = [[0] * (n+1) for _ in range(k+1)]

for i in range(n+1):
    dp[1][i] = 1

for i in range(2, k+1):
    for j in range(n+1):
        for l in range(j+1):
            dp[i][j] += dp[i-1][j-l]
            dp[i][j] %= int(1e9)

print(dp[k][n])


# 탑다운 방식의 재귀 풀이는 실패
# def recur(n, k, total):
#     if total > n:
#         return 0
#
#     print(n, k, total)
#     if k == 0:
#         if n == total:
#             return 1
#         else:
#             return 0
#
#
#     result = 0
#     for i in range(n+1):
#         result += recur(n, k-1, total+i) % 1000000000
#     return result
#
#
# print(recur(n, k, 0))

