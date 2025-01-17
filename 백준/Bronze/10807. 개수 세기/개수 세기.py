N = int(input())
numList = []
numList = list(map(int, input().split(" ")))
count = 0

findNum = int(input())
for num in numList :
    if findNum == num :
        count += 1
print(count)