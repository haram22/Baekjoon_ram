def solution(n):
    answer = 0
    result = ''
    str_num = list(str(n))
    str_num.sort(reverse = True)
    for i in range(len(str_num)) :
        result += str_num[i]
    return int(result)