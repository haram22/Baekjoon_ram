h, m = map(int, input().split())
time = (h * 60 + m) - 45
finH = time // 60
finM = time % 60
if finH < 0 :
    finH += 24
print(finH, finM)
