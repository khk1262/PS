'''
The following algorithm generates the next permutation lexicographically after a given permutation. It changes the given permutation in-place.

Find the largest index k such that a[k] < a[k + 1]. If no such index exists, the permutation is the last permutation.
Find the largest index l greater than k such that a[k] < a[l].
Swap the value of a[k] with that of a[l].
Reverse the sequence from a[k + 1] up to and including the final element a[n].
'''

import sys

input = sys.stdin.readline
N = int(input())
a = list(map(int, input().split()))
f = -1
for i in range(N-1):
    if a[i] < a[i+1]:
        f = i
if f == -1:
    print(f)
else:
    for j in range(N-1, -1, -1):
        if a[j] > a[f]:
            a[f], a[j] = a[j], a[f]
            break
    result = a[:f+1] + list(reversed(a[f+1:]))
    print(*result)