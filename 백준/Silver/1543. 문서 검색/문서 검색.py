S = input()
F = input()
count = 0
newS = S
while(1) :
    if F in newS :
        newS = S.replace(F, '_')
        count += 1
    else :
        break
print(newS.count('_'))