a = list(map(ord, list(input().strip())))
b = list(map(ord, list(input().strip())))

a.sort()
b.sort()

a_n = len(a)
b_n = len(b)
i = j = 0
count = 0

while i < a_n and j < b_n:
    if a[i] == b[j]:
        i += 1
        j += 1
    elif a[i] > b[j]:
        j += 1
        count += 1
    else:
        i += 1
        count += 1
while j < b_n:
    j += 1
    count += 1
while i < a_n:
    i += 1
    count += 1

print(count)