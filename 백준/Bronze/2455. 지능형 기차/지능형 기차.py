totalList = []
total = 0
for i in range(4) :
    n, size = list(map(int, input().split(' ')))
    total = total + size - n
    totalList.append(total)
print(max(totalList))