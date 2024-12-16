def solution(numbers):
    answer = -1
    list_num = [0,1,2,3,4,5,6,7,8,9]
    for i in range(9) :
        for j in range(len(numbers)) :
            if i+1 == numbers[j] :
                list_num.remove(i+1)
        
    return sum(list_num)