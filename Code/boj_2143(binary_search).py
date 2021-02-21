import sys
import bisect

input = sys.stdin.readline


def b_search(arr, num, want, start=0, end=None):
    ans = 0
    if end is None:
        end = len(arr) - 1

    while start <= end:
        mid = (start + end) // 2

        if arr[mid] + num >= want:
            end = mid - 1
            if arr[mid] + num == want:
                ans += 1
        else:
            start = mid + 1
    return ans


T = int(input())
n = int(input())

a = [0] * (n + 1)

temp = list(map(int, input().split()))
for i in range(1, n+1):
    a[i] = a[i-1] + temp[i-1]

m = int(input())

b = [0] * (m + 1)

temp = list(map(int, input().split()))
for i in range(1, m+1):
    b[i] = b[i-1] + temp[i-1]

a_sum = []
b_sum = []

for i in range(1, n+1):
    for j in range(i):
        a_sum.append(a[i] - a[j])

for i in range(1, m+1):
    for j in range(i):
        b_sum.append(b[i] - b[j])

a_sum.sort()
b_sum.sort()

result = 0
for i in range(len(a_sum)):
    low = bisect.bisect_left(b_sum, T - a_sum[i])
    high = bisect.bisect_right(b_sum, T - a_sum[i])

    result += (high - low)

print(result)
