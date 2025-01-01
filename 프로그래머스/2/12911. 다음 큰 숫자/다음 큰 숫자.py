def solution(n):
    answer = ''
    numberof1 = 0
    continue_num = 0
    result_num1 = 0
    strN = bin(n).replace('0b', '')
    for i in range(len(strN)) :
        if strN[i] == '1' :
            numberof1 += 1
    while (1) :
        n += 1
        answer_bin = ''
        addStr = bin(n).replace('0b', '')
        result_num1 = 0
        for i in range(len(addStr)) :
            if addStr[i] == '1' :
                result_num1 += 1
        if result_num1 == numberof1 :
            answer_bin = '0b' + addStr
            print(result_num1, n)
            answer = n
            break
    return answer