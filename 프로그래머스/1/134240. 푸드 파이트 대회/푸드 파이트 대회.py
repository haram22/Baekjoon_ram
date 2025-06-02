def solution(food):
    count = 0
    a = []
    b = []
    a_answer = ''
    b_answer = ''
    for i in range(1, len(food)) :
        count = food[i] // 2
        a.append(count)
        b.append(count)
    
    for i in range(len(a)) :
        for j in range(a[i]) :
            a_answer += str(i+1)
    
    for i in range(len(a_answer)-1, -1, -1) :
        b_answer += a_answer[i]
    
    return a_answer + '0' + b_answer