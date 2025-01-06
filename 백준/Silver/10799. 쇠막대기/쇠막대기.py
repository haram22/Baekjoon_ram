user_input = input()
stack = []
count = 0
for i in range(len(user_input)) :
    if user_input[i] == '(' :
        stack.append(i)
    else :
        if stack[-1] == i-1 :
            stack.pop()
            count += len(stack)
        else :
            stack.pop()
            count += 1
print(count)