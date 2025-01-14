user_input = input()

for i in range(len(user_input)) :
    print(user_input[i], end='')
    if (i+1) % 10 == 0 :
        print("")
print("")