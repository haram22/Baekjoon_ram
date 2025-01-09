userInput = []
userInput = input().split()

ascend = 0
descend = 0
for i in range(len(userInput)-1) :
    if int(userInput[i])+1 == int(userInput[i+1]) :
        ascend += 1
    if int(userInput[i])-1 == int(userInput[i+1]) :
        descend += 1
if ascend == 7 :
    print("ascending")
elif descend == 7 :
    print("descending")
else :
    print("mixed")