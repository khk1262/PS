import sys

input = sys.stdin.readline


def ccw(p1, p2, p3):
    return (p2[0]-p1[0])*(p3[1]-p1[1]) - (p3[0]-p1[0])*(p2[1]-p1[1])


p1 = tuple(map(int, input().split()))
p2 = tuple(map(int, input().split()))
p3 = tuple(map(int, input().split()))

result = ccw(p1, p2, p3)

if result > 0:
    print(1)
elif result < 0:
    print(-1)
else:
    print(0)
