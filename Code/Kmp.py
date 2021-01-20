import sys

'''
불일치 하였을때 건너뛰기를 하기위한 함수
'''
def getPi(p):
    n = len(p); j = 0
    li = [0 for _ in range(n)]

    for i in range(1, n):
        while j > 0 and p[i] != p[j]:
            j = li[j-1]
        if p[i] == p[j]:
            j += 1
            li[i] = j
    return li


def kmp(s, p):
    pi = getPi(p)
    n = len(s); m = len(p); j = 0
    ans = []
    for i in range(n):
        while j > 0 and s[i] != p[j]:
            j = pi[j-1]
        if s[i] == p[j]:
            if j == m-1:
                ans.append(i-m+1)
                j = pi[j]
            else:
                j += 1
    return ans


T = sys.stdin.readline().rstrip()
P = sys.stdin.readline().rstrip()

result = kmp(T, P)

print(len(result))
for i in result:
    print(i+1)