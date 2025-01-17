N = int(input())
F = {1 : 0, 2 : 1, 3 : 1}

def minCount(N) :
    if N not in F :
        if N % 2 == 0 and N % 3 == 0 :
            minValue = min(minCount(N/2), minCount(N/3)) + 1
        elif N % 3 == 0 :
            minValue = min(minCount(N/3), minCount(N-1)) + 1
        elif N % 2 == 0 :
            minValue = min(minCount(N/2), minCount(N-1)) + 1
        else :
            minValue = minCount(N-1) + 1
        F[N] = minValue
    return F[N]

print(minCount(N))