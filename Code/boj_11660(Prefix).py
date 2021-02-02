import sys
input = sys.stdin.readline

N, M = map(int, input().split())
result = 0
prefix = [[0 for col in range(N+2)] for row in range(N+2)]

for i in range(1, N+1):
    temp = list(map(int, input().split()))
    for j in range(1, len(temp)+1):
        prefix[i+1][j+1] = prefix[i][j+1] + prefix[i+1][j] - prefix[i][j] + temp[j-1]

for j in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    result = prefix[x2+1][y2+1] - prefix[x2+1][y1] - prefix[x1][y2+1] + prefix[x1][y1]
    print(result)
