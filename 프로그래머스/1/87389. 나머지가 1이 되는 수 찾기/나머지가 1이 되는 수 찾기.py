def solution(n):
    answer = 0
    answer_list = []
    for i in range(n) :
        if (i != 0 and n % i == 1) :
            answer_list.append(i)
    answer = min(answer_list)
    return answer