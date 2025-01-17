N = int(input())

for i in range(N) :
    for j in range(N) :
        if i % 2 != 0 and j == 0 :
            print(" ", end='')
        print("*", end='')
        print(" ", end='')
    print("")