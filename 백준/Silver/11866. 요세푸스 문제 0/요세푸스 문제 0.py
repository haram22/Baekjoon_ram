import sys
N, K = map(int, sys.stdin.readline().split(' '))
numList = [x for x in range(1, N+1)]
index = 0

ans = []
while (numList) :
    index = (index + K - 1) % len(numList) 
    ans.append(numList[index])
    numList.pop(index)
print("<", end='')
for i in range(len(ans)) :
    if i < len(ans)-1 :
        print(ans[i], end=', ')
    else :
        print(ans[i], end='')
print(">")