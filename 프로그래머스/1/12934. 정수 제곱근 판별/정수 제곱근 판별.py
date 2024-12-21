def solution(n):
    answer = n**(1/2)
    is_int = str(answer)
    if is_int[-1] != '0' and is_int[-2] != '.' :
        return -1
    else :
        return (answer + 1) ** 2