def solution(A,B):
    list_len = len(A)
    result_list = [0] * list_len
    sums = 0
    
    A.sort()
    B.sort()
    
    for i in range(list_len) :
        sums += A[i] * B[len(A)-i-1]
        result_list[i] = sums
        list_len -= 2

    return sums
