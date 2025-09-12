def solution(answers):
    answer = [0, 0, 0]
    p = [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    for j in range(3) :
        for i in range(len(answers)) :
            if answers[i] == p[j][i % len(p[j])] :
                answer[j] += 1  
    
    max_score = max(answer)
    result = [i+1 for i, s in enumerate(answer) if s == max_score]
    return result
                