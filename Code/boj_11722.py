N = int(input())
li = list(map(int, input().split()))

dp = [1 for _ in range(N)]

result = 1001
for i in range(N):
    for j in range(i):


print(result)