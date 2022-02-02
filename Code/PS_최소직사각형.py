def solution(sizes):
    h, v = 0, 0

    for i in sizes:
        if i[0] > i[1]:
            h = max(h, i[0])
            v = max(v, i[1])
        else:
            h = max(h, i[1])
            v = max(v, i[0])

    return h*v


print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))