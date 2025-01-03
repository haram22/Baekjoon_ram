size, count = input().split(' ')
ball = [i for i in range(1, int(size)+1)] 
for i in range(int(count)) :
    temp = []
    n1, n2 = input().split(' ')
    index1 = int(n1)-1
    index2 = int(n2)-1
    temp = ball[index2]
    ball[index2] = ball[index1]
    ball[index1] = temp
for i in range(len(ball)) :
    print(ball[i], end=' ')
print("")