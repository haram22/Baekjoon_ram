N = int(input())
a = []
b = []
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a.sort()
b.sort(reverse=True)
fin = 0
for i in range(len(a)) :
    fin += (a[i] * b[i])
print(fin)