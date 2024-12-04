def solution(a, b, c, d):
    answer = 0
    dice_set = set()
    dice_set.update([a,b,c,d])
    same_num = 0
    
    # set으로 바꾸고 그 갯수에 따라 구분?
    # set으로 하면, 
    # # case1) 모두 같은 숫자인 경우
    # # case2) 세 숫자가 같은 숫자인 경우 (1,1,1,2) -> (10 × p + q)^2
    # # case3) 두개 씩 같은 숫자인 경우 (2,2,3,3) -> (p + q) × |p - q|
    # # case4) 두 숫자만 같은 경우 (1,1,2,3) -> q × r
    # # case5) 모두 다른 숫자 나오는 경우 (1,2,3,4) -> min(a,b,c,d)
    
    # case 1
    if (len(dice_set) == 1) :
        answer = 1111 * a
    # case 5
    elif (len(dice_set) == 4) :
        answer = min(a,b,c,d)
    # case 4
    elif (len(dice_set) == 3) :
        # 여기에선 같은 숫자가 뭔지만 찾으면 된다
        same_num = check_multi_num(a,b,c,d)
        dice_set.discard(same_num)
        final = list(dice_set)
        answer = final[0] * final[1]
    # case 2,3
    else : 
        # case 2
        if (a == b == c) :
            answer = ((10 * a) + d) ** 2
        elif (a == c == d) :
            answer = ((10 * a) + b) ** 2
        elif (a == b == d) :
            answer = ((10 * a) + c) ** 2
        elif (b == c == d) :
            answer = ((10 * b) + a) ** 2
        # case 3
        else :
            print("case 3")
            if (a == b) :
                answer = (a + c) * abs(a - c)
            elif (a == c) :
                answer = (a + b) * abs(a - b)
            elif (a == d) :
                answer = (a + b) * abs(a - b)
    return answer

# 0번째에는 집합 개수, 많이 나온 순서대로 정렬해주는 함수를 만들어야하나
def check_multi_num(a,b,c,d) :
    same_num = 0
    for i in range(4) :
            if ((a == b) or (a == c) or (a == d)) :
                same_num = a
            elif ((b == c) or (b == d)) :
                same_num = b
            elif ((c == d)) :
                same_num = c
            else :
                same_num = d
    return same_num