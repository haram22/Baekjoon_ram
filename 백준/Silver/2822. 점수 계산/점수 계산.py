score = []
copyScore = []
for i in range(8) :
    a = int(input())
    score.append(a)
    copyScore.append(a)
copyScore.sort(reverse=True)
maxList = []

for i in range(5) :
    maxList.append(copyScore[i])
print(sum(maxList))

for i in range(8) :
    for j in range(5) :
        if maxList[j] == score[i] :
            print(i+1, end=' ')
print()

