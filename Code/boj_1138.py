import sys

input = sys.stdin.readline

n = int(input())
li = list(map(int, input().split()))

temp = [0] * n
for i in range(len(li)):
    t = 0
    vo = 0
    while True:
        if temp[t] == 0 and vo == li[i]:
            temp[t] = i + 1
            break
        if temp[t] == 0:
            vo += 1
        t += 1
print(*temp)