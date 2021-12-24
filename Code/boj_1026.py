import sys

input = sys.stdin.readline

n = int(input())
one = list(map(int, input().split()))
two = list(map(int, input().split()))

one.sort()
two.sort()
two.reverse()

sum = 0

for i in range(len(one)):
    sum += (one[i] * two[i])
print(sum)