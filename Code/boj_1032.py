n = int(input())
li = [input() for _ in range(n)]
test = list(zip(*li))

cnt = ''

for i in test:
    if len(set(i)) != 1:
        cnt += '?'
    else:
        cnt += i[0]
print(cnt)