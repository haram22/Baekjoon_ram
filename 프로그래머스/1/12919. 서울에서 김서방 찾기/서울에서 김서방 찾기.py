def solution(seoul):
    answer = ''
    for i in range(len(seoul)) :
        if seoul[i] == 'Kim' :
            print(f"김서방은 {i}에 있다")
            answer = f"김서방은 {i}에 있다"
    return answer