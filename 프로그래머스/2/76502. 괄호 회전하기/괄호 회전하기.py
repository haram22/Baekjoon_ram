def solution(s):
    answer = 0
    len_s = len(s)
    s = s*2
    for i in range(len_s) :
        ss = s[i:i+len_s]
        if check_true(ss) == len_s / 2:
            answer += 1
    return answer

def check_true(ss) :
    opens = ['(', '[', '{']
    close = [')', ']', '}']
    stack_open = []
    count = 0
    for i in range(len(ss)) :
        pop = ''
        if ss[i] in opens :
            stack_open.append(ss[i])
        if len(stack_open) != 0 :
            if ss[i] in close :
                pop = stack_open.pop()
                if pop == '(' :
                    if ss[i] == ')' :
                        count += 1
                elif pop == '[' :
                    if ss[i] == ']' :
                        count += 1
                elif pop == '{' :
                    if ss[i] == '}' :
                        count += 1
                else :
                    return count
    return count

