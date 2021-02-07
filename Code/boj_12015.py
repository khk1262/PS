import sys

input = sys.stdin.readline
output = sys.stdout.write

def biset(arr, num, start=0, end=None):
    if end is None:
        end = len(arr) - 1

    while start < end:
        mid = (start + end) // 2
        if arr[mid] < num:
            start = mid + 1
        else:
            end = mid
    return end


def solve():
    N = int(input())
    li = list(map(int, input().split()))

    answer = []

    for i in range(N):
        if not answer:
            answer.append(li[i])
        elif answer[-1] < li[i]:
            answer.append(li[i])
        elif answer[-1] > li[i]:
            temp = biset(answer, li[i])
            answer[temp], li[i] = li[i], answer[temp]

    return len(answer)


output(str(solve()))
