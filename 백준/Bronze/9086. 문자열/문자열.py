a = int(input())

str_list = []

for i in range(a):
    b = input()
    str_list.append(b)

for j in range(a):
    count = len(str_list[j])
    print(str_list[j][0]+str_list[j][count-1])