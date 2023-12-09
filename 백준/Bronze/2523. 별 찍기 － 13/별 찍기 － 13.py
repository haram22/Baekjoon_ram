a = int(input())
for i in range(a):
    for p in range(i+1):
            print("*", end="")
    print("\n", end="")
for i in range(a-1):
    for p in range(a-i-1):
        print("*", end="")
    print("\n", end="")