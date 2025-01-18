N = int(input())
numList = []
result = []
for i in range(N) :
    numList.append(list(map(int, input().split(' '))))

for i in range(N) :
    numList[i].sort()
    result.append(numList[i][-3])

for num in result :
    print(num)