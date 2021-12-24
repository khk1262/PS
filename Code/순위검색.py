def solution(info, query):
    answer = []
    info_temp = [info[i].split(' ') for i in range(len(info))]
    query_temp = [query[i].split(' ') for i in range(len(query))]
    query_temp = [[item for item in query_temp[j] if item != 'and'] for j in range(len(query_temp))]

    print(info_temp)
    print(query_temp)

    temp = [[] for _ in range(len(query_temp))]

    for i in range(len(query_temp)):
        for j in range(len(query_temp[i])-1):
            if query_temp[i][j] != '-':
                temp[i].append(j)
        print(temp)

    for q in range(len(query_temp)):
        check = True
        for inf in info_temp:
            for t in temp[q]:
                if query_temp[q][t] != inf[t]:
                    check = False



    return answer

print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"],
               ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))