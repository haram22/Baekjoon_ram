def solution(my_string):
    answer = ''
    my_string = my_string.lower()
    list_str = list(my_string)
    list_str.sort()
    for i in range(len(list_str)) :
        answer += list_str[i]
    return answer