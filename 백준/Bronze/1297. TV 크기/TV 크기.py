import math
D, H, W = map(int, input().split(' '))
x = math.sqrt(D**2 / (H**2 + W**2))
print(math.floor(x * H), math.floor(x * W))
