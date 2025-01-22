N = int(input())
result = []
def penlin(n) :
    strN = str(n)
    rstrN = ''
    for i in range(len(strN)-1, -1, -1) :
        rstrN += strN[i]
    if int(rstrN) == int(strN) :
        return print("YES")
    else :
        return print("NO")
    
for i in range(N) :
    rn = ''
    n = input()
    for j in range(len(n)-1, -1, -1) :
        rn += str(n[j])
    result.append(int(n) + int(rn))
for i in range(len(result)) :
    penlin(result[i])


