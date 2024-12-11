def solution(a, b):
    answer = 0
    ans_list = []
    if a > b :
        for i in range(a - b + 1) :
            ans_list.append(i + b)
    elif a < b :
        for i in range(b - a + 1) :
            ans_list.append(i + a)
    else :
        return a
    
    answer = sum(ans_list)
    return answer