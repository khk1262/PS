'''
계속 문제를 틀린 이유 - N이 1e6까지 넣을 수 있고 이보다 크거나 같은 소수를 구할 수 있어야하는데,
멍청하게 소수를 1e6정도까지만 구해서 틀림 범위를 2*1e6까지 올리고 맞음
'''

num = 2*1e6
is_prime = [0, 0] + [1 for i in range(int(num)-1)]
prime = []


def check(li):
    a = str(li)
    half = len(a) // 2

    for i in range(half):
        if a[i] != a[len(a) - i - 1]:
            return False
    return True


for i in range(2, int(num)+1):
    if is_prime[i] != 0:
        prime.append(i)
        for j in range(2*i, int(num)+1, i):
            is_prime[j] = 0

N = int(input())

for i in prime:
    if i >= N:
        if check(i):
            print(i)
            break

