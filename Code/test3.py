def solution(cakes, cut_rows, cut_columns):
    answer = 0

    cakes_temp = list(map(list, cakes))

    for i in range(len(cut_rows)-1):
        for j in range(len(cut_columns)-1):
            row_one, row_two = cut_rows[i], cut_rows[i+1]
            col_one, col_two = cut_columns[j], cut_columns[j+1]

            if i == 0:
                if j == 0:
                    temp = cakes_temp[0:row_one+1][0:col_one+1]
                elif j == len(cut_columns)-2:
                    temp = cakes_temp[0:row_one + 1][col_two:]
                else:
                    temp = cakes_temp[0:row_one + 1][col_one:col_two+1]
            elif i == len(cut_rows):
                if j == 0:
                    temp = cakes_temp[row_two:][0:col_one+1]
                elif j == len(cut_columns)-2:
                    temp = cakes_temp[row_two:][col_two:]
                else:
                    temp = cakes_temp[row_two:][col_one:col_two+1]
            else:
                temp = cakes_temp[row_one:row_two+1][col_one:col_two+1]



            print(temp)



    return answer


cakes = ["AAAACX", "AAAACX", "AAAACX", "ZZZZZX", "ATTTTX", "XUUUUU"]
row = [1, 2, 4]
col = [2, 3]

print(solution(cakes, row, col))