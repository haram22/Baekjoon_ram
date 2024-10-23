def solution(ineq, eq, n, m):
    answer = 0
    # 먼저 받은 문자에 따라 비교
    if ineq == '<' :
        # <=
        if eq == '=' :
            if n <= m :
                answer = 1
            else :
                answer = 0
        # <!
        else :
            if m > n :
                answer = 1
            else :
                answer = 0
    else : # >
        # >=
        if eq == '=' :
            if n >= m :
                answer = 1
            else :
                answer = 0
        # >!
        else :
            if m < n :
                answer = 1
            else :
                answer = 0
    return answer