N, M = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()
left = 0
right = max(arr)
while(left < right):
    mid = (left+right+1)//2
    sum = 0
    for i in arr:
        if i-mid >= 0 : sum += i-mid
    if sum >= M:
        left = mid
    else:
        right = mid - 1
print(left)