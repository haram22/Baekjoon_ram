def solution(x):
    answer = True
    str_num = str(x)
    sum_num = 0
    for i in range(len(str_num)) :
        sum_num += int(str_num[i])
    print(sum_num)
    
    if x % sum_num == 0 :
        answer = True
    else :
        answer = False
    return answer