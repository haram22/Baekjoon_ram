import math
N = int(input())
result = []
for i in range(N) :
    a, b = map(int, input().split(' '))
    result.append(math.lcm(a, b))
for c in result :
    print(c)