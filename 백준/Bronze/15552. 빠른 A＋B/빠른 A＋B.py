import sys
N = int(sys.stdin.readline())
final = []
for i in range(N) :
    a, b = map(int, sys.stdin.readline().split(' '))
    final.append(a + b)

for total in final :
    print(total)