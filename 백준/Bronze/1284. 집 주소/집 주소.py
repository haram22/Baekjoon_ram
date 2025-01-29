ans = []
while(1) :
    N = input()
    if N == '0' :
        break
    nums = 0
    for i in range(len(N)) :
        if N[i] == '1' :
            nums += 2
        elif N[i] == '0' :
            nums += 4
        else :
            nums += 3
    nums += len(N) + 1
    ans.append(nums)
for an in ans :
    print(an)
