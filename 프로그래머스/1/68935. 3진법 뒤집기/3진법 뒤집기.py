def solution(n):
    answer = 0
    ramn = []
    while(n > 0) :
        ramn.append(n%3)
        n = n // 3
    ramn.reverse()
    for i in range(len(ramn)) :
        if ramn != 0 :
            answer += (3 ** i)*ramn[i]
    return answer