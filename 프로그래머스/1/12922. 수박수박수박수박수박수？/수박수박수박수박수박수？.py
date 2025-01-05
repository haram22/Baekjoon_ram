def solution(n):
    answer = ''
    str1 = '수'
    str2 = '박'
    for i in range(n) :
        if i % 2 == 0 :
            answer += str1
        else :
            answer += str2
    return answer