def solution(a, d, included):
    answer = 0
    list_len = len(included)
    
    for i in range(list_len):
        if (included[i] == True):
            answer += a+ (d*i)
    
    return answer