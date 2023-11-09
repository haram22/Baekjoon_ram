a = []
sum = 0
for i in range(5):
    a.append(int(input()))
    if a[i] < 40 :
        a[i] = 40
for j in range(5):
    sum += a[j]
print(int(sum/5))