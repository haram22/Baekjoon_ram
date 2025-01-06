user_input = []
for i in range(9) :
    user_input.append(int(input()))
    
totalSum = 0
flag = 0
num_list = []
for i in range(len(user_input)) :
    totalSum += int(user_input[i])
    num_list.append(int(user_input[i]))

height = 0
for i in range(len(num_list)) :
    if flag == 1 :
        break
    for j in range(i+1, len(num_list)) :
        if totalSum - (num_list[i] + num_list[j]) == 100 :
            not1 = num_list[i]
            not2 = num_list[j]
            num_list.remove(not1)
            num_list.remove(not2)
            flag = 1
            break
num_list.sort()

for num in num_list:
    print(num)