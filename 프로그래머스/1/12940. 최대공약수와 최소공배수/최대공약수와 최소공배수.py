def solution(n, m):
    answer = []
    first = n
    second = m
    r = 0
    while(m != 0) :
        r = n % m
        n = m
        m = r
    answer.append(n)
    answer.append(first * second / n)
        
    return answer