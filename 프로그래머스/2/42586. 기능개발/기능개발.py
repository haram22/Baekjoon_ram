import math
def solution(progresses, speeds):
    answer = []
    days = []
    for i in range(len(progresses)) :
        days.append(math.ceil((100-progresses[i]) / speeds[i]))
    print("->", days)
    
    current = days[0]  
    count = 1
    
    for i in range(1, len(days)) :
        if days[i] <= current :
            count += 1
        else :
            answer.append(count)
            current = days[i]
            count = 1
    
    answer.append(count)
    return answer