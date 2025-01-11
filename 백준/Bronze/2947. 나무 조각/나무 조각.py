k = list(map(int, input().split(' ')))
result = []
for i in range(len(k)) :
    for j in range(len(k)-1) :
        if k[j] >= k[j+1] :
            temp = k[j]
            k[j] = k[j+1]
            k[j+1] = temp
            result+=k
for i in range(len(result)) :
    if i != 0 :
        if (i) % 5 == 0 :
            print('\n', end='')
    print(result[i], end=' ')
print("")