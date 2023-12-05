a = int(input())

for i in range(a):
    for d in range(a-i-1):
        print(" ", end="")
    for e in range(i):
        print("*", end="")
        print("*", end="")
    print("*",end="")
    print("\n", end="")

for i in range(a-1):
    for d in range(i+1):
        print(" ", end="")
    for e in range(a-i-2):
        print("*", end="")
        print("*", end="")
    print("*",end="")
    print("\n", end="")