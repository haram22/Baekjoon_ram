N = int(input())
final = []
for i in range(N) :
    num = input().split(' ')
    result = float(num[0])

    for j in range(len(num)) :
        if num[j] == '@' :
            result = result * 3
        elif num[j] == '%' :
            result = result + 5
        elif num[j] == '#' :
            result = result - 7
    final.append(f'{result:.2f}')
    
for i in range(len(final)) :
    print(final[i])