def solution(n):
    answer = []
    answer.append(n)
    while(n != 1) :
#         짝수일 때
        if (n%2 == 0) :
            n = n/2
            answer.append(int(n))
        else :
            n = 3*n+1
            answer.append(int(n))
    print(answer)
    return answer