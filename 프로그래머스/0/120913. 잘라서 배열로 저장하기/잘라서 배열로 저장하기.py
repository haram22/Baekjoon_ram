def solution(my_str, n):
    answer = []
    new_str = ''
    count = (len(my_str) + n - 1) // n
    for i in range(count) :
        if i >= count :
            answer.append(my_str[i*n :])
        answer.append(my_str[i*n : i*n + n])
    return answer