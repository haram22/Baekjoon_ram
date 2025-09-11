def solution(nums):
    answer = 0
    len_num = len(set(nums))
    for i in range(len_num, -1, -1) :
        if i <= int(len(nums)/2) :
            return i