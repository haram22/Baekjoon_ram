N = int(input())
line = 1
while N > line :
    N -= line
    line += 1
if line % 2 != 0 :
    mom = line - (N-1)
    son = N
else :
    mom = N
    son = line - (N-1)

print(f'{mom}/{son}')