import sys
info = [ [0] * 4] * 5
sums = [0] * 5
for i in range(5) : 
    info[i] = list(map(int, sys.stdin.readline().split(' ')))
    sums[i] = sum(info[i])
winner = max(sums)
winner_index = sums.index(winner)
print(winner_index+1, winner)

