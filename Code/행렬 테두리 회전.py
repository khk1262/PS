def solution(rows, columns, queries):
    answer = []
    table = [[(columns*i+j) for j in range(1,columns+1)] for i in range(rows)]
    for q in queries:
        x1, y1, x2, y2 = q[0] - 1,q[1] - 1,q[2] - 1,q[3] - 1
        min_v = 99999999

        for col in range(y1, y2):
            if col == y1:
                temp1 = table[x1][col+1]
                table[x1][col+1] = table[x1][col]
            else:
                temp2 = table[x1][col+1]
                table[x1][col + 1] = temp1
                temp1 = temp2
            min_v = min(min_v, table[x1][col+1])

        for row in range(x1, x2):
            temp2 = table[row+1][y2]
            table[row+1][y2] = temp1
            temp1 = temp2
            min_v = min(min_v, table[row+1][y2])

        for col in range(y2, y1, -1):
            temp2 = table[x2][col - 1]
            table[x2][col - 1] = temp1
            temp1 = temp2
            min_v = min(min_v, table[x2][col-1])

        for row in range(x2, x1, -1):
            temp2 = table[row-1][y1]
            table[row-1][y1] = temp1
            temp1 = temp2
            min_v = min(min_v, table[row-1][y1])

        answer.append(min_v)
    return answer

print(solution(3,3,[[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]]	))