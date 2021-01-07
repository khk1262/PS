K, N = map(int, input().split())
lan = []

for _ in range(K):
    lan.append(int(input()))

result = 0
left = 1
right = pow(2, 31) - 1

while left <= right:
    sum = 0

    mid = (right + left) // 2
    for i in range(K):
        sum += lan[i] // mid

    if sum >= N:
        result = max(result, mid)
        left = mid + 1

    else:
        right = mid - 1

print(result)