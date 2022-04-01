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


for i in range(n):
    li.append(list(map(int, input().split())))

li.sort()


dp = [li[0][1]]
idx = 0
stack = [[0, li[0][1]]]


for i in range(1, n):
    if dp[idx] < li[i][1]:
        dp.append(li[i][1])
        idx+=1
        stack.append([idx, li[i][1]])
    else:
        ii = lower_bound(dp, idx, li[i][1])
        dp[ii] = li[i][1]
        stack.append([ii, li[i][1]])

print(n -len(dp))