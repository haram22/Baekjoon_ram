nums = []
for i in range(3) :
    nums += list(map(int, input().split()))
result = nums[0] * nums[1] * nums[2]
strNum = str(result)

numlist = [x for x in range(0,10)]
count = [0] * 10

for i in range(len(strNum)) :
    if int(strNum[i]) in numlist :
        count[int(strNum[i])] += 1

for i in range(len(count)) :
    print(count[i])