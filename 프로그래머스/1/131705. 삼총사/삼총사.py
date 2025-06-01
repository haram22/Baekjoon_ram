from itertools import combinations
        
def solution(number):
    answer = 0
    comList = list(combinations(number, 3))
    for i in range(len(comList)) :
        if sum(comList[i]) == 0 :
            answer += 1
    return answer