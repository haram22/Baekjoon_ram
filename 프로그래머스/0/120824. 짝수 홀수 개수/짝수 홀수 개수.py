def solution(num_list):
    answer = []
    count_1 = 0
    count_2 = 0
    for i in range(len(num_list)) :
        if (num_list[i] % 2 == 0) :
            count_2 += 1
        else :
            count_1 += 1
    answer.append(count_2)
    answer.append(count_1)
    return answer