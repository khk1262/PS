import sys

input = sys.stdin.readline

N, C = map(int, input().split())

li = []

for i in range(N):
    li.append(int(input()))

li.sort()

