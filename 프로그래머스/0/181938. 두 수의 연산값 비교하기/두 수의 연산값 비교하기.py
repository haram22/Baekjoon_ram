def solution(a, b):
    answer = 0
    result_ab = ""
    result_2ab = ""
    
    result_ab = int(str(a) + str(b))
    result_2ab = 2*a*b
    
    answer = int(max(result_ab, result_2ab))
    return answer