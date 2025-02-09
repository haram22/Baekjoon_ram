def solution(array):
    answer = []
    max_ = 0
    idx = 0
    for i in range(len(array)) :
        if array[i] >= max_ :
            max_ = array[i]
            idx = i
    answer.append(max_)
    answer.append(idx)
    return answer