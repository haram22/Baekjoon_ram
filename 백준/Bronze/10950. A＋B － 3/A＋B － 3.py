N = int(input())
result = []
for i in range(N) :
    n1, n2 = map(int, input().split(' '))
    result.append(n1 + n2)

for i in range(N) :
    print(result[i])