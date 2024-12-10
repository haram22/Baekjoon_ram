def solution(n):
    answer = 0
    list_n = list(str(n))
    
    for i in range(len(list_n)) :
        answer += int(list_n[i])

    return answer