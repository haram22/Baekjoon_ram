N = int(input())
nums = []
answer = []
for i in range(N) :
    inputNum = int(input())
    binNum = bin(inputNum)
    listNum = list(binNum[2:])
    listNum.reverse()
    for j in range(len(listNum)) :
        if listNum[j] == '1' :
            answer.append(j)
for n in answer :
    print(n, end=' ')
print()