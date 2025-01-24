import sys
from itertools import *
N = int(sys.stdin.readline())
cardList = []
maxList = []
sumList = [] * N
# print(sumList)
for i in range(N) :
    cardList.append(list(map(int, input().split(' '))))
    # print(list(combinations(cardList[i], 3)))
    caseList = list(combinations(cardList[i], 3))
    max1 = 0
    maxNum = 0
    for j in range(len(caseList)) :
        if max1 < (sum(caseList[j]) % 10) :
            max1 = (sum(caseList[j]) % 10)
            maxNum = sum(caseList[j])
    maxList.append(max1)
    sumList.append(maxNum)

for i in range(N-1, -1, -1) :
    if maxList[i] == max(maxList) :
        print(i+1)
        break
