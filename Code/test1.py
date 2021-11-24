def solution(character, monsters):
    answer = ''
    c_heal, c_atk, c_prt = map(int, character.split())
    max_exp = 0

    for m in monsters:
        m_list = m.split()
        m_name, m_exp, m_heal, m_atk, m_prt = m_list[0], *list(map(int, m_list[1:]))
        time = 0

        while m_heal > 0:
            time += 1
            player_t = c_atk - m_prt
            monster_t = m_atk - c_prt

            if player_t > 0:
                m_heal -= player_t
            else:
                break

            if monster_t > 0:
                c_heal -= monster_t
                if c_heal <= 0:
                    break
                c_heal += monster_t

        if m_heal <= 0:
            result = m_exp / time
            if max_exp <= result:
                max_exp = result
                answer = m_name

    return answer


ch = "10 5 2"
mon = ["Knight 3 10 10 3","Wizard 5 10 15 1","knight 1 1 15 1"]

print(solution(ch, mon))