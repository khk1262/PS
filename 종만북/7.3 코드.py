# 카라츠바 알고리즘

def normalize(num):
    num.append(0)

    for i in range(len(num)-1):
        num[i+1] += num[i] // 10
        num[i] = num[i] % 10

    while len(num) > 1 and num[-1] == 0: num.pop()

    return num

def multiply(a, b):
    c = [0] * (len(a) + len(b) + 1)
    for i in range(len(a)):
        for j in range(len(b)):
            c[i+j] += a[i] * b[j]

    normalize(c)
    return c


print(multiply([4,3,2,1], [8,7,6,5]))
