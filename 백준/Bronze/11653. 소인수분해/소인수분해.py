N = int(input())
mok = 2
ans = []
def div(N, mok) :
    while(1) :
        if N % mok == 0 :
            ans.append(mok)
            N = N/mok
        else :
            break
    return N

while(N > 1) :
    N = div(N, mok)
    mok += 1
for n in ans :
    print(n)