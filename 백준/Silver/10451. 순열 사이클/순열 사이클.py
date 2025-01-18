N = int(input())
value = [] * N
index = [] * N
for i in range(N) :
    size = int(input())
    valueNum = list(map(int, input().split(' ')))
    value.append(valueNum)
    indexList = []
    for j in range(size) :
        indexList.append(j+1)
    index.append(indexList)

countList = []
for j in range(N) :
    count = 0
    for i in range(len(value[j])) :
        if value[j][i] != 0 :
            count += 1
            root = index[j][i]
            while(1) :
                next = value[j][root-1]
                if root == 0 :
                    break
                else :
                    value[j][root-1] = 0
                    index[j][i] = 0
                    root = next
                # print(">>", value[j])
    countList.append(count)
for count in countList :
    print(count)