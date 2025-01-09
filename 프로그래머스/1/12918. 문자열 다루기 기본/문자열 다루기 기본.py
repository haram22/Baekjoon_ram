def solution(s):
    answer = True
    count_alpha = 0
    count_num = 0
    if len(s) == 4 or len(s) == 6 :
        for i in range(len(s)) :
            if (ord(s[i]) >= 65 and ord(s[i]) <= 90) or (ord(s[i]) >= 97 and ord(s[i]) <= 122) :
                count_alpha += 1
            else :
                count_num += 1
        if count_alpha == len(s) or count_num == len(s):
            answer = True
        else :
            answer = False
    else :
        answer = False
    return answer
    
