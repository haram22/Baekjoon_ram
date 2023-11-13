import math
li = []
for i in range(5):
    ans = int(input())
    li.append(ans)

answer = max(math.ceil(li[1]/li[3]), math.ceil(li[2]/li[4]))
print(li[0]-answer)