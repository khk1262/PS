from itertools import combinations

def solution(relation):
    answer = 0
    temp = list(zip(*relation))
    temp2 = []
    a_list = []

    for i in range(len(temp)):
        if len(temp[i]) != len(set(temp[i])):
            temp2.append(temp[i])
        else:
            answer += 1
    sample = [i for i in range(len(temp2))]
    for t in range(2, len(temp2)+1):
        combi = list(combinations(sample, t))
        for com in combi:
            com_list = [[] for _ in range(len(temp2[0]))]

            for c in com:
                for j in range(len(temp2[0])):
                    com_list[j] += temp2[c][j]
                    com_list = list(map(''.join, com_list))

            if len(com_list) == len(set(com_list)):
                if not a_list:
                    answer += 1
                    a_list.append(list(com))
                else:
                    check = True
                    for t in a_list:
                        if set(com) & set(t) == set(t):
                            check = False
                    if check:
                        answer += 1
                        a_list.append(list(com))
    return answer




print(solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]))