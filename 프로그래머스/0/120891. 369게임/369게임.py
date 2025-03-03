def solution(order):
    answer = 0
    str_order = str(order)
    for i in range(len(str_order)) :
        if str_order[i] in '369' :
            answer += 1
    return answer