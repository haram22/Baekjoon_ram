# 20 7 23 19 10 15 25 8 13

user_input = []
for i in range(9) :
    user_input.append(int(input()))
    
totalSum = 0
flag = 0
for i in range(len(user_input)) :
    totalSum += int(user_input[i])

for i in range(len(user_input)) :
    if flag == 1 :
        break
    for j in range(i+1, len(user_input)) :
        if totalSum - (user_input[i] + user_input[j]) == 100 :
            not1 = user_input[i]
            not2 = user_input[j]
            user_input.remove(not1)
            user_input.remove(not2)
            flag = 1
            break
user_input.sort()

for num in user_input:
    print(num)