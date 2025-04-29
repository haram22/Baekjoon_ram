num_list = []
while (1) :
    a = input()
    if a == '0' :
        break
    else :
        num_list.append(a)

answer = []
for i in range(len(num_list)) :
    stack = []
    stack1 = []
    if (len(num_list[i]) % 2 == 0 ) :
        for j in range(int(len(num_list[i]) / 2)) :
            stack.append(num_list[i][j])
        for j in range(len(num_list[i])-1, int(len(num_list[i]) / 2)-1, -1) :
            stack1.append(num_list[i][j])
        
    else :
        for j in range(int(len(num_list[i]) / 2)) :
            stack.append(num_list[i][j])
        for j in range(len(num_list[i])-1, int(len(num_list[i]) / 2), -1) :
            stack1.append(num_list[i][j])
    if stack == stack1 :
            answer.append("yes")
    else :
        answer.append("no")
for a in answer :
    print(a)