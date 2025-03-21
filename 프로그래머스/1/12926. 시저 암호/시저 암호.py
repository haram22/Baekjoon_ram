def solution(s, n):
    answer = ''
    num = 0
    for i in range(len(s)) :
        num = ord(s[i]) + n
        # 소문자이면
        if s[i].islower() :
            if num >= 97 and num <= 122 :
                answer += chr(num)
            else :
                answer += chr(97 + (num - 122) - 1)
        # 대문자이면
        elif s[i].isupper() :
            if num <= 90 :
                answer += chr(num)
            else :
                answer += chr(65 + (num - 90) - 1)
        else :
            answer += ' '
    return answer