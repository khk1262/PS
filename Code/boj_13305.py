N = int(input())
dis = list(map(int, input().split()))
oil = list(map(int, input().split()))
oil.pop()

small = oil[0]
result = (dis[0] * small)

for i in range(1, N-1):
    if oil[i] < small:
        small = oil[i]
    result += (dis[i] * small)

print(result)