import sys
N, K = map(int, sys.stdin.readline().split(' '))
numList = []
for i in range(N) :
    numList.append(int(sys.stdin.readline()))

path = []
count = 0
pick = 0
while K not in path :
    path.append(pick)
    pick = numList[pick]
    count += 1

    if count > N :
        count = 0
        break

print(count - 1)