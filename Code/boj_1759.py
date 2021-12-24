import sys

mo = ['a', 'e', 'i', 'o', 'u']

L, C = map(int, input().split())
li = input().split()
li.sort()


def passwd(start, m_c, c_c, sen, c):
    if c == L:
        if m_c > 0 and c_c > 1:
            print(sen)
        return
    for i in range(start+1, len(li)):
        sen += li[i]
        if li[i] in mo:
            passwd(i, m_c+1, c_c, sen, c+1)
        else:
            passwd(i, m_c, c_c+1, sen, c+1)
        sen = sen[:-1]


for j in range(C - L + 1):
    if li[j] in mo:
        passwd(j, 1, 0, li[j], 1)
    else:
        passwd(j, 0, 1, li[j], 1)
