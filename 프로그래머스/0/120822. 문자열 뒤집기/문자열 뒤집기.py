def solution(my_string):
    answer = ''
    answer_list = []
    for i in range(len(my_string)) :
        last_char = my_string[len(my_string)-1-i]
        answer += last_char
    return answer