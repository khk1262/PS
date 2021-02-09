import sys

input = sys.stdin.readline


def lower_bound(arr, num, start=0, end=None):
    if end is None:
        end = len(arr) - 1

    while start < end:
        mid = (start + end) // 2

        if arr[mid] >= num:
            end = mid
        else:
            start = mid + 1
    return end


def upper_bound(arr, num, start=0, end=None):
    if end is None:
        end = len(arr) - 1

    while start < end:
        mid = (start + end) // 2

        if arr[mid] > num:
            end = mid
        else:
            start = mid + 1
    return end


def solve():
    N = int(input())
    f_li = list(map(int, input().split()))
    M = int(input())
    s_li = list(map(int, input().split()))

    f_li.sort()

    for i in range(M):
        lower = lower_bound(f_li, s_li[i])
        upper = upper_bound(f_li, s_li[i])
        if upper == N - 1 and f_li[N - 1] == s_li[i]:
            upper += 1

        print(upper - lower, end=' ')

solve()