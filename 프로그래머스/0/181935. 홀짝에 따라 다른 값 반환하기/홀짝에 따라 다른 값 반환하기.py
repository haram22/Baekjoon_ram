def solution(n):
    answer = 0
    if n%2 == 0 :
        print("짝수")
        for i in range(n) :
            if (i+1) % 2 == 0 :
                answer += (i+1)**2
    else :
        for i in range(n) :
            if (i+1) % 2 != 0 :
                answer += i+1
        
    return answer