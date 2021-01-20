import sys

N, M = map(int, sys.stdin.readline().split())
sum_list = [0 for _ in range(N+1)]

a = list(map(int, sys.stdin.readline().split()))

for i in range(1, N+1):
    sum_list[i] = sum_list[i-1] + a[i-1]

for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    print(sum_list[j] - sum_list[i-1])