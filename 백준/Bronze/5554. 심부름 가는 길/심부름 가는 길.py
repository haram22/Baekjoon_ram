a = []
sum = 0
for i in range(4):
    a.append(int(input()))
    sum += a[i]
print(int(sum/60))
print(sum%60)