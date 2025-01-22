N = int(input())
strList = []

for i in range(N) :
    word = input()
    jword = ''.join(set(word))
    strList.append(jword)
    

sums = [0] * N
ans = []
for i in range(N) :
    for j in range(len(strList[i])) :
        sums[i] += ord(strList[i][j])
    ans.append(1950+65 - sums[i])

for i in ans :
    print(i)