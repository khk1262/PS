def solution(time, gold, upgrade):
    answer = -1

    for m in range(len(upgrade)):
        cur_item = upgrade[0][1]
        cur_money = 0
        t = 0
        t_time = time
        up_cnt = 1
        while t_time:
            t_time -= 1
            t += 1
            if t == cur_item:
                cur_money += gold
                t = 0

            while up_cnt <= m and cur_money >= upgrade[up_cnt][0]:
                cur_money -= upgrade[up_cnt][0]
                cur_item = upgrade[up_cnt][1]
                up_cnt += 1

        answer = max(answer, cur_money)

    return answer


time = 11
gold = 1000
upgrade = [[0, 5], [100, 4], [200, 3]]

print(solution(time, gold, upgrade))