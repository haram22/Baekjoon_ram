N = int(input())
nums = list(map(int, input().split(' ')))
setNum = list(set(nums))
setNum.sort()
for n in setNum :
    print(n, end=' ')
print('')