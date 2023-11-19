num1, num2 = input().split()
price = int(input())
sumnum = int(num1) + int(num2)
if price*2 > sumnum:
    print(sumnum)
else :
    print(sumnum-price*2)