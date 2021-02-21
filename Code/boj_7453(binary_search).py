import sys
import bisect
input = sys.stdin.readline

n = int(input())
A = [0] * n
B = [0] * n
C = [0] * n
D = [0] * n
for i in range(n):
    A[i], B[i], C[i], D[i] = map(int,input().split())

AB = list()
CD = list()

for i in A:
    for j in B:
        AB.append(i+j)
for i in C:
    for j in D:
        CD.append(i+j)

AB.sort()
CD.sort()

count = 0
ans = 1
for i in range(len(AB)):
    temp = bisect.bisect_left(CD,-AB[i])
    if temp == len(CD):
        print(f'temp = {temp}')
        continue
    if (i == len(AB) - 1) or AB[i] != AB[i+1]:
        if CD[temp] == -AB[i]:
            count += (bisect.bisect_right(CD, -AB[i]) - temp) * ans
            ans = 1
    else:
        if CD[temp] == -AB[i]:
            ans += 1
print(count)