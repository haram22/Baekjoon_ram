def solution(sides):
    answer = 0
    maxNum = max(sides)
    sides.remove(maxNum)
    if sides[0] + sides[1] > maxNum :
        answer = 1
    else :
        answer = 2
    return answer