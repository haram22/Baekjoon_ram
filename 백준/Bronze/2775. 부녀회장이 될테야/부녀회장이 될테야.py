import sys
N = int(sys.stdin.readline())
step = []
room = []

def findNum(step, room) :
    F = [ [0] * 14 ]
    # 초기화
    for i in range(step) :
        F.append([0] * 14)
        F[i][0] += 1
        for i in range(14) :
            F[0][i] = i+1
    # 계산
    for i in range(1, step+1) :
        for j in range(1, room+1) :
            F[i][j] = F[i-1][j] + F[i][j-1]
    # print(F)
    return F[step][room] + 1

for i in range(N) :
    stepN = int(sys.stdin.readline())
    step.append(stepN)
    roomN = int(sys.stdin.readline())-1
    room.append(roomN)


for i in range(N) :
    print(findNum(step[i], room[i]))