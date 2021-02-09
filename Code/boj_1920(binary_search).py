import sys

input = sys.stdin.readline


def b_search(arr, num, start=0, end=None):
    if end is None:
        end = len(arr) - 1

    while start <= end:
        mid = (start + end) // 2

        if arr[mid] > num:
            end = mid - 1
        elif arr[mid] == num:
            return 1
        else:
            start = mid + 1
    return 0


N = int(input())
f_li = list(map(int, input().split()))
f_li.sort()

M = int(input())
s_li = list(map(int, input().split()))

for num in s_li:
    print(b_search(f_li, num))
