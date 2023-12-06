a = int(input())

for i in range(a-1):
    for j in range(i+1):
        print("*", end="")
    for k in range(a-i-1):
        print(" ", end="")
    for k in range(a-i-1):
        print(" ", end="")
    for j in range(i+1):
        print("*", end="")
    print("\n", end="")
    
for i in range(a*2):
    print("*", end="")
print("\n", end="")

for i in range(a-1):
    for j in range(a-i-1):
        print("*", end="")
    for k in range(i+1):
        print(" ", end="")
    for k in range(i+1):
        print(" ", end="")
    for j in range(a-i-1):
        print("*", end="")
    print("\n", end="")
