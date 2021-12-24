import sys

sum = 0
li = []
for _ in range(7):
    a = int(input())
    if a % 2 == 1:
        sum += a
        li.append(a)

if sum: print(sum)
print(min(li) if li else -1)
