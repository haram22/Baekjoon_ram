def solution(slice, n):
    answer = 0
    answer = n // slice
    if answer * slice < n :
        answer += 1
    return answer