import math
def findNum(number) :
    cnt = 0
    for i in range(1, int(math.sqrt(number))+1) :
        if number % i == 0 :
            cnt += 1
            if i != number // i :
                cnt += 1
    return cnt

def solution(number, limit, power):
    answer = 0
    count = []
    count.append(1)
    for i in range(2, number+1) :
        count.append(findNum(i))
    for i in range(len(count)) :
        if limit < count[i] :
            count[i] = power
    return sum(count)