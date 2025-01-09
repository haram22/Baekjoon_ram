import sys
N = int(sys.stdin.readline())
oriList = []
for _ in range(N):
    name, dd, mm, yy = sys.stdin.readline().split()
    oriList.append([int(yy), int(mm), int(dd), name])
oriList.sort()
print(oriList[-1][3])
print(oriList[0][3])