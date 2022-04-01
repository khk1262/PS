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
li = []
val_arr = []

for i in range(n):
    li.append(list(map(int, input().split())))
    val_arr.append(li[-1][0])

li.sort()


dp = [li[0][1]]
idx = 0
track = [[0, li[0][1], li[0][0]]]


for i in range(1, n):
    if dp[idx] < li[i][1]:
        dp.append(li[i][1])
        idx+=1
        track.append([idx, li[i][1], li[i][0]])
    else:
        ii = lower_bound(dp, idx, li[i][1])
        dp[ii] = li[i][1]
        track.append([ii, li[i][1], li[i][0]])

stack = []
temp = idx


for i in range(n-1, -1, -1):
    if temp == track[i][0]:
        stack.append(track[i][2])
        temp-=1


print(n - len(dp))

val_arr = list(set(val_arr) - set(stack))

for i in val_arr:
    print(i) 