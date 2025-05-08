stackList = []
answer = []
def push_num(num) :
    stackList.append(num)

def pop_num() :
    if len(stackList) < 1 :
        answer.append(-1)
    else :
        answer.append(stackList.pop())

def print_size() :
    answer.append(len(stackList))

def isEmpty() :
    if len(stackList) < 1 :
        answer.append(1)
    else :
        answer.append(0)

def print_top() :
    if len(stackList) < 1 :
        answer.append(-1)
    else :
        answer.append(stackList[-1])

N = int(input())
for i in range(N) :
    user_input = input()
    flag = user_input[0] + user_input[1]
    if flag == 'pu' :
        user_input = user_input[5:]
        push_num(int(user_input))
    elif flag == 'po' :
        pop_num()
    elif flag == 'si' :
        print_size()
    elif flag == 'to' :
        print_top()
    else :
        isEmpty()
    
for i in answer :
    print(i)