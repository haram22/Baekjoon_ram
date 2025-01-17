N = int(input())
nums = []
for i in range(N) :
    nums.append(int(input()))
for i in range(N) :
    if nums[i] % 2 == 0 :
        print("even")
    else :
        print("odd")