li = []
minFirst = []
a, b, c = input().split()
li.append(int(a))
li.append(int(b))
li.append(int(c))

minFirst = sorted(li)
print(minFirst[0], minFirst[1], minFirst[2])