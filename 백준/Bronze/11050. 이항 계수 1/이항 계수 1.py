a, b = map(int, input().split(' '))

top = 1
for i in range(b) :
    top *= (a-i)

def factorial(b) :
    if b < 2 :
        return 1
    else :
        return factorial(b-1) * b
bottom = factorial(b)

print(int(top/bottom))