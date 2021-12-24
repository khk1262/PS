import sys

input = sys.stdin.readline
li = list(map(int, input().split()))
count = 1
index = 0

for i in range(3):
    if count < li.count(li[i]):
        count = li.count(li[i])
        index = i

if count == 1:
    print(max(li) * 100)
elif count == 2:
    print(li[index]*100 + 1000)
else:
    print(10000+li[index]*1000)
