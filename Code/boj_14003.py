import sys
input = sys.stdin.readline


def lower_bound(li, idx, i):
    f = -1
    e = idx + 1
    while f + 1 < e:
        mid = f + ( e - f ) // 2
        
        if li[mid] >= i:
            e = mid
        else:
            f = mid
    return e



n = int(input())
li = list(map(int, input().split()))

dp = [li[0]]
track = [(0, li[0])]
idx = 0

for i in range(1, len(li)):

    if dp[idx] < li[i]:
        dp.append(li[i])
        idx+=1
        track.append((idx, li[i]))

    else:
        ii = lower_bound(dp, idx, li[i])
        dp[ii] = li[i]
        track.append((ii, li[i]))

temp = idx

stack = []

for i in range(n-1, -1, -1):
    if temp == track[i][0]:
        stack.append(track[i][1])
        temp-=1

print(len(stack))
stack.reverse()
print(*stack)