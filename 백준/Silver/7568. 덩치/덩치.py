import sys
N = int(input())
users = []
for i in range(N) :
    users.append(list(map(int, sys.stdin.readline().split(' '))))

rank = [1] * len(users)
for i in range(N) :
    for j in range(N) :
        if users[i][0] < users[j][0] and users[i][1] < users[j][1] :
            rank[i] += 1

for i in rank :
    print(i, end=' ')
print("")