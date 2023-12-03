a = int(input())
for i in range(a):
    for t in range(a-i-1):
        print(" ", end="")
    print("*",end="")
    for j in range(i):
        print("*", end="")
        print("*", end="")
    print("\n", end="")