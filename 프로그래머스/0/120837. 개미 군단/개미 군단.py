def solution(hp):
    answer = 0
    while(hp > 0) :
        mok = 0
        if hp >= 5 :
            mock = hp // 5
            answer += mock
            hp -= (5 * mock)
        elif hp >= 3 :
            mock = hp // 3
            answer += mock
            hp -= (3 * mock)
        else :
            mock = hp // 1
            answer += mock
            hp -= (1 * mock)
    return answer