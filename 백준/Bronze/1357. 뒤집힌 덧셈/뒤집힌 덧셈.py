a,b = input().split()
sum = ''
listA = list(a)
listB = list(b)
listA.reverse()
listB.reverse()
a = int(''.join(listA))
b = int(''.join(listB))

sum = a+b
listSum = list(str(sum))
listSum.reverse()
sumStr = int(''.join(listSum))
print(sumStr)