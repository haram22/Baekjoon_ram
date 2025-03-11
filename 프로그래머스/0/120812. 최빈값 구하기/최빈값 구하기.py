def solution(array):
    answer = 0
    count = [0] * (max(array) + 1)
    for i in array :
        count[i] += 1
    max_num = 0
    for c in count :
        if c == max(count) :
            max_num += 1
            answer = count.index(max(count))
    if max_num > 1 :
        answer = -1
    return answer