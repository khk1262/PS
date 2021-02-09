import sys

input = sys.stdin.readline


def b_search(arr, string, start=0, end=None):
    if end is None:
        end = len(arr) - 1

    while start <= end:
        mid = (start + end) // 2

        if arr[mid][1] > string[1]:
            end = mid - 1
        elif arr[mid][0] == string[0]:
            return 1
        else:
            start = mid + 1
    return 0



N, M = map(int, input().split())

listen = []; see = []

for _ in range(N):
    string = input().rstrip()
    temp = list(string)
    result = 0
    for i in range(len(temp)):
        result += (ord(temp[i]) - ord('a') + 1) * (30 ** (20 - i))

    listen.append((string, result))

for _ in range(M):
    string = input().rstrip()
    temp = list(string)
    result = 0
    for i in range(len(temp)):
        result += (ord(temp[i]) - ord('a') + 1) * (30 ** (20 - i))
    see.append((string, result))

listen.sort()
see.sort()

answer = []
for s in see:
    if b_search(listen, s):
        answer.append(s[0])

print(len(answer))
print('\n'.join(answer))
