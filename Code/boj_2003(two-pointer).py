N, M = map(int, input().split())
li = list(map(int, input().split()))

result = 0; total = 0; lo = 0; hi = 0

while lo < N:
    if total >= M or hi == N:
        total -= li[lo]
        lo += 1
    else:
        total += li[hi]
        hi += 1
    if total == M:
        result += 1
print(result)
