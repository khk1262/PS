import sys
input = sys.stdin.readline


class MaxHeap(object):
    def __init__(self):
        self.data = [0]

    def insert(self, data):
        self.data.append(data)
        l = len(self.data) - 1

        while l > 1:
            if self.data[l] > self.data[(l//2)]:
                self.data[l], self.data[(l//2)] = self.data[(l//2)], self.data[l]
                l = l // 2
            else:
                break

    def remove(self):
        if len(self.data) > 2:
            self.data[1], self.data[-1] = self.data[-1], self.data[1]
            data = self.data.pop()
            self.heapify(1)
        elif len(self.data) == 2:
            data = self.data.pop()
        else:
            data = 0
        return data

    def heapify(self, i):
        l = 2*i
        r = (2*i) + 1
        large = i
        l_exist = r_exist = False

        if l < len(self.data) and self.data[l] > self.data[i]:
            l_exist = True
        if r < len(self.data) and self.data[r] > self.data[i]:
            r_exist = True

        if l_exist and r_exist:
            if self.data[l] > self.data[r]:
                self.data[i], self.data[l] = self.data[l], self.data[i]
                large = l
            else:
                self.data[i], self.data[r] = self.data[r], self.data[i]
                large = r

        elif l_exist:
            self.data[i], self.data[l] = self.data[l], self.data[i]
            large = l
        elif r_exist:
            self.data[i], self.data[r] = self.data[r], self.data[i]
            large = r
        else:
            return

        return self.heapify(large)


heap = MaxHeap()
N = int(input())
for _ in range(N):
    x = int(input())
    if x == 0:
        print(heap.remove())
    else:
        heap.insert(x)


# import heapq
# import sys
#
#
# input = sys.stdin.readline
#
# heap = []
# N = int(input())
#
# for _ in range(N):
#     x = int(input())
#     if x == 0:
#         if len(heap) > 0:
#             print(heapq.heappop(heap))
#         else:
#             print(0)
#     else:
#         heapq.heappush(heap, x)