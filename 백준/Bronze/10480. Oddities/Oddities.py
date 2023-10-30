# 1. 입력 개수 입력받기
# 2. input_str에 순서대로 입력받은 수 저장하기
# 3. 입력 받음과 동시에 짝수(1)인지, 홀수(0)인지 구분하여 1 또는 0 저장
# 4. 짝수이면 even, 홀수이면 odd 출력하기

num = int(input())
input_list = []
result = []

for i in range(num):
    input_str = int(input())
    input_list.append(input_str)
    if (int(input_list[i]) % 2 == 0) :
        result.append(1) # 짝수
    else :
        result.append(0) # 홀수

for i in range(num):
    if (result[i] == 1):
        print(input_list[i], "is even")
    else :
        print(input_list[i], "is odd")