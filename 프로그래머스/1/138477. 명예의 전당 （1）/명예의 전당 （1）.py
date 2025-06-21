def solution(k, score):
    answer = []
    range_list = []
    for i in range(1, len(score)+1) :
        range_list = score[:i]
        range_list.sort()
        fin_list = range_list[-k:]
        answer.append(fin_list[0])
    return answer