a, b = map(int, input().split())
min_num = min(a,b)
yaksu = []
baesu = 0
answer = []
for i in range(1, min_num+1) :
    if a % i == 0 and b % i == 0 :
        yaksu.append(i)
answer.append(yaksu[-1])
answer.append(int(a*b/yaksu[-1]))

for i in answer :
    print(i)