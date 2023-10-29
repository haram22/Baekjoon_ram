num = int(input())
input_list = []
sort_len = []
result = []

for i in range(num):
    inputstr = input()
    input_list.append(inputstr)

sort_len = list(set(input_list)) # 중복 제거
# 두 개 이상의 조건을 기준으로 분류할 때, x: (길이순, 순서대로)
result = sorted(sort_len, key=lambda x: (len(x), x))

for i in range(len(result)):
    print(result[i])