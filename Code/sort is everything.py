def selection_sort(arr):
    n = len(arr)
    for i in range(n-1):
        small = i

        for j in range(i+1, n):
            if arr[j] < arr[small]:
                small = j
        if i != small:
            arr[i], arr[small] = arr[small], arr[i]


def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        small = arr[i]
        j = i - 1
        while j >= 0 and small < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = small


li = [8, 5, 6, 2, 4]
insertion_sort(li)
print(*li)