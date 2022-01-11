n, k = map(int, input().split())

li = [i for i in range(1, n+1)]
temp = k - 1
print('<', end='')
while li:
    if len(li) == 1:
        print(f"{li.pop()}>")
        break
    temp = temp % (len(li))
    print(f"{li.pop(temp)},", end=' ')
    temp += (k-1)
