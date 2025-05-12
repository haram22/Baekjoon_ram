s = set()
N = int(input())
a = list(map(int, input().split()))
for i in range(N) :
    s.add(a[i])
M = int(input())
b = list(map(int, input().split()))
for i in range(M) :
    if b[i] in s :
        print("1")
    else :
        print("0")