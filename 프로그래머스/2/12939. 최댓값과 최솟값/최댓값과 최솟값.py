def solution(s):
    answer = ''
    min_num = 0
    max_num = 0
    num_list = []
    
    str_list = s.split(' ')
    print(str_list)
    for i in range(len(str_list)) :
        num_list.append(int(str_list[i]))
    print(num_list)
    min_num = min(num_list)
    max_num = max(num_list)
    # answer += min_num
    # answer += max_num
    print(min_num, max_num)
    answer += str(min_num)
    answer += " "
    answer += str(max_num)
    print("answer=", answer)
    return answer