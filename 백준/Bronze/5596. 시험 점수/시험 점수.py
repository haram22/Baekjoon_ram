list1 = []
list2 = []
a, b, c, d = input().split()
a1, b1, c1, d1 = input().split()
sum1 = 0
sum2 = 0
list1.append(int(a))
list1.append(int(b))
list1.append(int(c))
list1.append(int(d))
list2.append(int(a1))
list2.append(int(b1))
list2.append(int(c1))
list2.append(int(d1))

sum1 = list1[0]+list1[1]+list1[2]+list1[3]
sum2 = list2[0]+list2[1]+list2[2]+list2[3]

if sum1>sum2:
    print(sum1)
elif sum1<sum2:
    print(sum2)
else:
    print(sum1)