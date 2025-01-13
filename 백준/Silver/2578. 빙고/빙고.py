bingo = [list(map(int, input().split())) for _ in range(5)]
answer = []
count = 0
total = 0

def isBingo(total) :
    forvertic = 0
    for1 = 0
    for2 = 0
    for i in range(5) :
        if bingo[i] == [0] * 5 :
            total += 1
    for i in range(5) :
        forvertic = 0
        for j in range(5) :
            if bingo[j][i] == 0 :
                forvertic += 1
        if forvertic == 5 :
            total += 1
    for i in range(5) : 
        if bingo[i][i] == 0 :
            for1 += 1
    if for1 == 5 :
        total += 1
    for i in range(5) :
        if bingo[i][4-i] == 0 :
            for2 += 1
    if for2 == 5 :
        total += 1
    return total


for i in range(5) :
    answer += list(map(int, input().split()))
for i in range(25) :
    for x in range(5) :
        for y in range(5) :
            if answer[i] == bingo[x][y] :
                bingo[x][y] = 0
                count += 1
    if count >= 12 :
        result = isBingo(total)
        if result >= 3 :
            print(i + 1)
            break
