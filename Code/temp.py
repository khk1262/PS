# def combination(arr, r):
#     arr = sorted(arr)
#     used = [0 for _ in range(len(arr))]
#
#     def generate(chosen):
#         if len(chosen) == r:
#             print(chosen)
#             return
#
#         start = arr.index(chosen[-1]) + 1 if chosen else 0
#         for nxt in range(start, len(arr)):
#             if used[nxt] == 0 and (nxt == 0 or arr[nxt - 1] != arr[nxt] or used[nxt - 1]):
#                 chosen.append(arr[nxt])
#                 used[nxt] = 1
#                 generate(chosen)
#                 chosen.pop()
#                 used[nxt] = 0
#     generate([])


# def quick_sort(arr):
#     def sort(l, r):
#         print(l, r)
#         if l < r:
#             p = partition(l, r)
#             print(p)
#             sort(l, p - 1)
#             sort(p+1, r)
#
#     def partition(l, r):
#         print('second', l, r)
#         pivot = arr[r]
#         i = l - 1
#
#         for j in range(l,r):
#             if arr[j] <= pivot:
#                 i += 1
#                 print('i',i)
#                 arr[i], arr[j] = arr[j], arr[i]
#         arr[i + 1], arr[r] = arr[r], arr[i + 1]
#         return i + 1
#
#     return sort(0, len(arr)-1)
#
#
def merge_sort(arr):
    def sort(low, high):
        if high - low >= 2:
            mid = low + (high - low) // 2
            sort(low, mid)
            sort(mid, high)
            print(mid)
            merge(low, mid, high)

    def merge(low, mid, high):
        temp = [0 for _ in range(high - low)]
        l, h, k = low, mid, 0

        while l < mid and h < high:
            if arr[l] < arr[h]:
                temp[k] = arr[l]
                l += 1
            else:
                temp[k] = arr[h]
                h += 1
            k += 1

        while l < mid:
            temp[k] = (arr[l])
            l += 1
            k += 1
        while h < high:
            temp[k] = (arr[h])
            h += 1
            k += 1

        for i in range(low, high):
            arr[i] = temp[i - low]

    return sort(0, len(arr))

test = [3,4,1,5,6,7,8,2,4,5]

# quick_sort(test)
merge_sort(test)
print(test)







# print(solution(6, [[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]], 4))