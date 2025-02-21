def solution(my_string):
    answer = []
    for i in range(len(my_string)) :
        if my_string[i].isdigit() :
            answer += my_string[i]
    for j in range(len(answer)) :
        answer[j] = int(answer[j])
    answer.sort()
    return answer