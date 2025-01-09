n = input().split()
result = 0
sumNum = 0
for i in range(len(n)) :
    sumNum += (int(n[i]) ** 2)
result = sumNum % 10
print(result)