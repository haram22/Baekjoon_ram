def solution(n):
    result = int(n ** (1/2))
    if result ** 2 == n :
        return 1
    else :
        return 2