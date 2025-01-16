a, b, c = map(int, input().split(' '))
money = 0
if a == b == c :
    money += 10000 + 1000 * a
elif a == b != c :
    money += 1000 + a*100
elif a != b == c :
    money += 1000 + b*100
elif a == c != b :
    money += 1000 + a*100
else :
    money += (max(a, b, c)) * 100
print(money)