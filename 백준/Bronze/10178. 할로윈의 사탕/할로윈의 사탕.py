N = int(input())
each = []
ramn = []
for i in range(N) :
    a, b = map(int, input().split(' '))
    each.append(a//b)
    ramn.append(a%b)
for i in range(len(each)) :
    print(f'You get {each[i]} piece(s) and your dad gets {ramn[i]} piece(s).')