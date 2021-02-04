N, M = map(int, input().split())
li = list(map(int, input().split()))

result = 0; total = 0; lo = 0; hi = 0

while True:
    if total >= M:
        total -= li[lo]
        lo += 1
    elif hi == N:
        break
    else:
        total += li[hi]
        hi += 1
    if total == M:
        result += 1
print(result)
