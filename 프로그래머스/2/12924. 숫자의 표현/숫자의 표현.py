def solution(n):
    count = 0
    end = 0
    sum_num = 0
    # 짝수인 경우, 홀수인 경우 나누기
    # 짝수인 경우, 
        # 절반으로 나누고, 1부터 계속 더해서 n이 되는경우 구하기
        # 그리고 마지막에 +1
    # 홀수인 경우,
        # 절반으로 나누고, 반올림 하고, 1부터 계속 더해서 n이 되는 경우 구하기
        # 그리고 마지막에 +2
    if n == 1 :
        count = 1
    elif n%2 != 0 :
        end = int(n/2 + 0.5)
        count += 2
    else :
        end = int(n/2)
        count += 1
        
    for i in range(1, end) :
        sum_num = 0
        for j in range(i, end) :
            sum_num += j
            if sum_num == n :
                count += 1
            if sum_num > n :
                for_check = []
                break
    return count