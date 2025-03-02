def solution(num, k):
    answer = 0
    strNum = str(num)
    strK = str(k)
    if strK in strNum :
        answer = strNum.find(strK) + 1
    else :
        answer = -1
    return answer