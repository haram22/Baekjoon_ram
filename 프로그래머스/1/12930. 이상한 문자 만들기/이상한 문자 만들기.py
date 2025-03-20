def solution(s):
    answer = ''
    str_list = []
    str_list = s.split(' ')
    print(str_list)
    for i in range(len(str_list)) :
        for j in range(len(str_list[i])) :
            if j % 2 == 0 :
                answer += str_list[i][j].upper()
            else :
                answer += str_list[i][j].lower()
        if i < len(str_list)-1 :
            answer += ' '
    return answer