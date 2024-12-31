def solution(s):
    answer = True
    input_list = list(s)
    # 여는 괄호를 계속 stack에 넣다가, 닫는 괄호가 나오면 스택에 있는 여는 괄호 하나 빼기.
    # 여는 괄호 스택이 빈 스택이 될 때까지 반복하기
    stack = []
    i = 0
    while(i < len(input_list)) :
        if input_list[i] == '(' :
            stack.append(input_list[i])
        else :
            if len(stack) == 0 :
                answer = False
                break
            else :
                stack.pop()
        i += 1
        
    if len(stack) != 0 :
        answer = False

    return answer