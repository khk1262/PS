h, m = map(int, input().split())
t = int(input())

h_t, m = divmod(m+t, 60)
h = (h+h_t) % 24
print(h, m)