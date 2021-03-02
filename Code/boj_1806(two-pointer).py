import sys

input = sys.stdin.readline


def sum_check(arr, check):
    s, e = 0, 0
    total = 0
    cnt = 0
    length = len(arr)
    result = int(1e5)
    while s < length:

        if total >= check or e == length:
            if total >= check:
                result = min(result, cnt)
            total -= arr[s]
            s += 1
            cnt -= 1
        else:
            total += arr[e]
            e += 1
            cnt += 1

    return result


N, M = map(int, input().split())
li = list(map(int, input().split()))
print(sum_check(li, M)) if sum_check(li, M) != int(1e5) else print(0)