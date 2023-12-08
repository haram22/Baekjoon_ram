a = int(input())
for i in range(a):
    for j in range(a-i-1):
        print(" ", end="")
    for p in range(i+1):
            print("*", end="")
    print("\n", end="")
for i in range(a-1):
    for j in range(i+1):
        print(" ", end="")
    for p in range(a-i-1):
        print("*", end="")
    print("\n", end="")