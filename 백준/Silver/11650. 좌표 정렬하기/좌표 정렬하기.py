N = int(input())
numList = []
for i in range(N) :
    numList.append(list(map(int, input().split(' '))))

numList.sort()
for num in numList :
    print(num[0], num[1])