import sys
N, K = map(int, sys.stdin.readline().split(' '))
numList = []
for i in range(N) :
    numList.append(int(sys.stdin.readline()))

path = []
pick = 0
count = -1

while K not in path :
    path.append(pick)
    pick = numList[pick]
    count += 1

    if count > N :
        count = -1
        break
print(count)