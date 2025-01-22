N = int(input())
cost = list(map(int, input().split(' ')))
ans = sum(cost) - max(cost)
print(ans)