a = int(input())
for i in range(a):
    for p in range(i):
        print(" ", end="")
    for t in range(a-i-1):
        print("*", end="")
        print("*", end="")
    print("*",end="")
    print("\n", end="")