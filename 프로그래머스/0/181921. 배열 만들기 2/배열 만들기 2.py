def solution(l, r):
    answer = []
    contain_list = []
    for i in range(l, r+1) :
        if (str(1) in str(i) or str(2) in str(i) or str(3) in str(i)
           or str(4) in str(i) or str(6) in str(i) or str(7) in str(i)
           or str(8) in str(i) or str(9) in str(i)) :
            continue
        else :
            contain_list.append(i)
    if (len(contain_list) == 0) :
        answer.append(-1)
    else :
        answer = contain_list
    return answer