import sys

last = 1e6 + 1
mod = 1e9 + 9
dp = [0] * int(last)

dp[1] = 1; dp[2] = 2; dp[3] = 4;

for i in range(4, int(last)):
    dp[i] = int((dp[i-3] + dp[i-2] + dp[i-1]) % mod)

c = int(sys.stdin.readline())

for _ in range(c):
    t = int(sys.stdin.readline())
    print(dp[t])
