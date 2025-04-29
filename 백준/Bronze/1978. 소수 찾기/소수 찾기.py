N = int(input())
nums = list(map(int, input().split()))
count = 0
if 2 in nums :
        count += 1
for i in nums :
    if i % 2 != 0 :
        each_count = 0
        each_list = []
        for j in range(1, round(i/2)+1) :
            if i % j == 0 :
                each_count += 1
                each_list.append(j)
        # print(i, each_count, each_list)
        if each_count == 1:
            count += 1
print(count)