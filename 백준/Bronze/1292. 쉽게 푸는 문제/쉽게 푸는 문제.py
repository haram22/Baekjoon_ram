a, b = map(int, input().split(' '))
numList = []
count = 1
while(1) :
    for i in range(count) :
        numList.append(count)
    count += 1
    if count > b :
        break
fin = sum(numList[a-1:b])
print(fin)