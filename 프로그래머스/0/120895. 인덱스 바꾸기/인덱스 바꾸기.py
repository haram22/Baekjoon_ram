def solution(my_string, num1, num2):
    answer = ''
    for i in range(len(my_string)) :
        if i == num1 :
            answer += my_string[:i]
            answer += my_string[num2]
            answer += my_string[i+1:num2]
            answer += my_string[num1]
            answer += my_string[num2+1:]
    return answer