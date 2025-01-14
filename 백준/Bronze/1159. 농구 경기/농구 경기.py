import sys
N = int(sys.stdin.readline())
nameList = []
for i in range(N) :
    name = sys.stdin.readline()
    nameList.append(name[0])
nameSet = list(set(nameList))
count = [0] * len(nameSet)

for i in range(N) :
    for j in range(len(nameSet)) :
        if nameList[i] == nameSet[j] :
            count[j] += 1

answer = ''
final = ''
last = ''
for i in range(len(nameSet)) :
    if count[i] >= 5 :
        answer+=nameSet[i]

if len(answer) == 0 :
    print("PREDAJA")
else :
    # print(answer)
    final = sorted(answer)
    # print(final)
    for i in range(len(final)) :
        last += final[i]
    # final = ''.join(answer)
    print(last)
