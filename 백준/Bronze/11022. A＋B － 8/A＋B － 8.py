N = int(input())
a = []
b = []
answer = []
for i in range(N) :
    aNum, bNum = map(int, input().split(' '))
    a.append(aNum)
    b.append(bNum)
    answer.append(aNum + bNum)
for i in range(N) :
    print(f'Case #{i+1}: {a[i]} + {b[i]} = {answer[i]}')
