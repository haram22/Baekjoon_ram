num = int(input())
users = []
for i in range(num) :
    users.append(input().split(' '))
    users[i][0] = int(users[i][0])
    
users.sort(key=lambda x:x[0])

for i in range(len(users)) :
    print(users[i][0],users[i][1])