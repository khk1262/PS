N, K = map(int, input().split())

li = [[0 for _ in range(N+1)] for _ in range(N+1)]

for i in range(N+1):
    for j in range(i+1):
        if j == 0 or j == i:
            li[i][j] = 1
        else:
            li[i][j] = (li[i-1][j-1] + li[i-1][j]) % 10007

print(li[N][K])
