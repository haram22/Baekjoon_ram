num = int(input())
for i in range(num):
    for t in range(i):
        print(" ",end="")
    for j in range(num-i):
        print("*", end="")
    print("\n", end="")