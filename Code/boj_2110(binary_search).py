import sys

input = sys.stdin.readline

N, C = map(int, input().split())
li = [int(input()) for _ in range(N)]

li.sort()

left, right = 0, int(1e9)
d = 0
while left + 1 < right:
    mid = (left + right) // 2
    start = li[0]
    cnt = 1
    for i in range(1, N):
        d = li[i] - start
        if mid <= d:
            cnt += 1
            start = li[i]

    print(mid, left, right, cnt)
    if cnt < C:
        right = mid
    else:
        left = mid

print(left)