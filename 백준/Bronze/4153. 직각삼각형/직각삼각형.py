answer = []
while (1) :
    sums = 0
    num_list = list(map(int, input().split()))
    if num_list[0] == 0 & num_list[1] == 0 & num_list[2] == 0 :
        break 
    max_num = max(num_list)
    for i in range(len(num_list)) :
        if num_list[i] >= max(num_list) :
            continue
        else :
            sums += (num_list[i] * num_list[i])
    if sums == max_num * max_num :
        answer.append('right')
    else :
        answer.append('wrong')
    
for i in answer :
    print(i)