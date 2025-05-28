def solution(d, budget):
    d.sort()
    count = 0
    for idx, cost in enumerate(d) :
        budget -= cost
        count += 1
        if budget < 0 :
            count -= 1
            break
    return count