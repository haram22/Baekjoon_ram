import math
def solution(n):
    answer = 0
    answer = round(n/7)
    if answer * 7 < n :
        answer += 1
    return answer