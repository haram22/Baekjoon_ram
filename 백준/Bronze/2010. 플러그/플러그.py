import sys
N = int(input())
multis = []
for i in range(N) :
    multis += list(map(int, sys.stdin.readline().split()))
for j in range(N-1) :
    multis[j] -= 1
print(sum(multis))