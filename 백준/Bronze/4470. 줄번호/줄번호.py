num = int(input())
strlist = []
for i in range(num):
    inputstr = input()
    strlist.append(inputstr)

for i in range(num):
    print(i+1, end='')
    print(". ", end='')
    print(strlist[i])