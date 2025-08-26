def solution(s):
    answer = []
    stack = ''
    char_idx = {}
    
    for i, char in enumerate(s) :
        if char in char_idx :
            answer.append(i-char_idx[char])
        else :
            answer.append(-1)
        char_idx[char] = i
        
    return answer
