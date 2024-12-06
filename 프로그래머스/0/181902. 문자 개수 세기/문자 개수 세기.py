def solution(my_string):
    answer = [0 for i in range(58)]
    str_list = list(my_string)
    for i in range(len(str_list)) :
        answer[ord(str_list[i]) - 65] += 1
    del answer[26:32]
    return answer



# 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,1,0,0,0,0,0,2,0,1,0,0,3,1,0,0,0,0,0,0

# 기댓값
# 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,1,0,0,0,0,0,2,0,1,0,0,3,1,0,0,0,0,0,0,0

# ASCII
# 91 - 96은 잘라야함
# A = 65
# a = 97
# z = 122