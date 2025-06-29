def solution(cards1, cards2, goal):
    answer = []
    for i in range(len(goal)) :
        if len(cards1) > 0 :
            if goal[i] == cards1[0] :
                print(goal[i])
                answer.append(goal[i])
                cards1.pop(0)
        if len(cards2) > 0 :
            if goal[i] == cards2[0] :
                print(goal[i])
                answer.append(goal[i])
                cards2.pop(0)
    
    if answer == goal :
        return 'Yes'
    else :
        return 'No'