import matplotlib.pyplot as plt
import random

n = int(1e3)
count = 0
x_list_circle, y_list_circle = [0] * n, [0] * n
x_list_out, y_list_out = [0] * n, [0] * n

for i in range(n):
    x = random.uniform(0, 1.0)
    y = random.uniform(0, 1.0)
    if (x**2+y**2) <= 1:
        x_list_circle[i] = x
        y_list_circle[i] = y
        count = count+1
    else:
        x_list_out[i] = x
        y_list_out[i] = y

print("파이값은? ", 4*count/n)

plt.plot(x_list_circle, y_list_circle, 'ro', x_list_out, y_list_out, 'bo')
plt.axis([0.0, 1.0, 0.0, 1.0])
plt.show()
