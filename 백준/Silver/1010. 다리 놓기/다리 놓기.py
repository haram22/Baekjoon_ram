def momFact(N, M) :
    fin = 1
    for i in range(N) :
        fin *= M-i
    return fin

def Factorial(N) :
    if N > 1 :
        return N * Factorial(N-1)
    else :
        return 1
 
n = int(input())

result = []
for i in range(n) :
    N, M = map(int, input().split(' '))
    n1 = momFact(N, M)
    n2 = Factorial(N)
    final = n1 / n2
    result.append(int(final))

for i in result :
    print(i)