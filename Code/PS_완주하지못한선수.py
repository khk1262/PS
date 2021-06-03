def solution(s,c):

    s.sort()
    c.sort()

    for par, com in zip(s, c) :
        if par != com :
            return par

    return s[-1]


pa_list = ["mislav", "stanko", "mislav", "ana"]
com = ["stanko", "ana", "mislav"]

print(solution(pa_list, com))