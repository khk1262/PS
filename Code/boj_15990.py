import sys
mod = 1e9 + 9
dp = [[0 for col in range(4)] for row in range(100001)]

'''
문제에서 말하는대로 같은 수가 2번 연속 나오지 않도록 구성하게되면
1은 1, 2는 2, 3은 1 2, 2 1, 3 으로 표현이 가능하다.
이때 dp는 각 수의 조합이 시작되는 수의 앞의 수대로 나눈 2차원 배열로 만들면
밑의 문장과 같다.
'''
dp[1][1] = 1; dp[2][2] = 1; dp[3][1] = 1; dp[3][2] =1; dp[3][3] = 1
'''
점화식은 다음과 같이 구상할 수 있다.
dp[i][1] = dp[i-1][2] + dp[i-1][3]
dp[i][2] = dp[i-2][1] + dp[i-2][3]
dp[i][3] = dp[i-3][1] + dp[i-3][2]

현재 구하고자 하는 수의 조합의 첫번째 자리 수에 따라 이전조합 시작 수가 정해진다. 
만약 현재 1부터 더해지는 조합일때 이전의 2, 3으로 시작하는 점화식
'''
for i in range(4, 100001):
    dp[i][1] = int((dp[i - 1][2] + dp[i - 1][3]) % mod)
    dp[i][2] = int((dp[i - 2][1] + dp[i - 2][3]) % mod)
    dp[i][3] = int((dp[i - 3][1] + dp[i - 3][2]) % mod)

T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    print(int(sum(dp[N]) % mod))