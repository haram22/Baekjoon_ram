def solution(n):
    answer = []
    answer_list = list(str(n))
    for i in range(len(answer_list)) :
        answer.append(int(answer_list[len(answer_list)-i-1]))
    return answer