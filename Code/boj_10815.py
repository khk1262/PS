def partition(l, r, li):
    pivot = li[r]
    i = l - 1

    for j in range(l, r):
        if li[j] < pivot:
            i+=1
            li[i], li[j] = li[j], li[i]
    li[i+1], li[r] = li[r], li[i+1]

    return i+1


def quicksort(l, r, li):
    if l < r:
        p = partition(l, r, li)

        quicksort(l, p-1, li)
        quicksort(p+1, r, li)


def b_search(s, e, target, li):
    if s > e:
        return 0
    else:
        mid = (s + e) // 2
        if target == li[mid]:
            return 1
        elif target < li[mid]:
            return b_search(s, mid - 1, target, li)
        elif target > li[mid]:
            return b_search(mid + 1, e, target, li)


N = int(input())
a = list(map(int, input().split()))

M = int(input())
b = list(map(int, input().split()))

quicksort(0, N-1, a)

for i in range(M):
    print(b_search(0, N-1, b[i], a), end=' ')
