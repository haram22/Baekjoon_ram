def solution(s):
    answer = ''
    index = 0
    if len(s) % 2 == 0 :
        index = int(len(s)/2)-1
        answer += s[index]
        answer += s[index + 1]
    else :
        index = int((len(s) - 1)/2)
        answer += s[index]
        
    return answer