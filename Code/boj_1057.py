import sys

input = sys.stdin.readline
n, a, b = map(int, input().split())
count = 0
while True:
    count += 1
    a = sum(divmod(a, 2))
    b = sum(divmod(b, 2))
    if a == b:
        print(count)
        break

