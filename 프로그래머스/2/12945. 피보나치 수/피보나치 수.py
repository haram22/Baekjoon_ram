def solution(n):
    list_fibo = [0] * (n+1)
    
    for i in range(n+1) :
        if i == 0 :
            list_fibo[i] += 0
        elif i == 1 :
            list_fibo[i] += 1
        else :
            list_fibo[i] += list_fibo[i-1] + list_fibo[i-2]

    return list_fibo[n] % 1234567
