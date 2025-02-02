h, m, s = map(int, input().split(':'))
hh, mm, ss = map(int, input().split(':'))

beforeSS = h*60*60 + m*60 + s
afterSS = hh*60*60 + mm*60 + ss

finSS = afterSS - beforeSS
if finSS < 0 :
    fh = finSS // 3600
    fh = fh + 24
else :
    fh = finSS // 3600
fm = (finSS % 3600) // 60
fs = finSS % 60 
print(f'{fh:02}:{fm:02}:{fs:02}')