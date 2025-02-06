N = int(input())

def total(n) :
    if n == 0 :
        return 0
    elif n == 1 :
        return 1
    else :
        return total(n-1) + n

scoreList = []
for i in range(N) :
    stack = []
    ans = input()
    count = 0
    score = 0
    for j in range(len(ans)) :
        if ans[j] == 'O' :
            count += 1
            stack.append(ans[j])
        elif ans[j] == 'X' :
            score += total(count)
            stack = []
            count = 0
        if j > len(ans)-2 :
            score += total(count)
    scoreList.append(score)
for s in scoreList :
    print(s)