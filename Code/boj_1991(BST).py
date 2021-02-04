import sys

input = sys.stdin.readline

N = int(input())

li = [[None, None] for i in range(N)]

for _ in range(N):
    a, b, c, = input().split()
    index = ord(a) - ord('A')
    left = ord(b) - ord('A')
    right = ord(c) - ord('A')
    li[index] = [left, right]


def pre_order(index = 0):
    if index < 0:
        return
    data = chr(index+ord('A'))
    print(data, end='')
    left = li[index][0]
    right = li[index][1]
    pre_order(left)
    pre_order(right)


def in_order(index = 0):
    if index < 0:
        return
    left = li[index][0]
    right = li[index][1]
    in_order(left)
    data = chr(index+ord('A'))
    print(data, end='')
    in_order(right)


def last_order(index = 0):
    if index < 0:
        return
    left = li[index][0]
    right = li[index][1]
    last_order(left)
    last_order(right)
    data = chr(index+ord('A'))
    print(data, end='')

pre_order()
print()
in_order()
print()
last_order()
