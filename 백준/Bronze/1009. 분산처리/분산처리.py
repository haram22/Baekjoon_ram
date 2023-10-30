#### 시간초과때문에 안됐다. 왜일까? 
# 1. 입력할 개수를 입력한다.
# 1.1 a 와 b를 입력받는다
# 2. a^b를 계산하고, 이를 10으로 나눈 나머지를 구한다.
# 3. 해당 나머지를 리스트에 넣는다.
# 4. 리스트 결과를 출력한다.

# num = int(input())
# result = []

# def cal(num1, num2):
#     final = 1
#     for i in range(num2):
#         final *= num1
#         final %= 10
#     return final

# for i in range(num):
#     a, b = map(int, input().split(" "))
#     result.append(cal(a,b))

# for i in range(num):
#     print(result[i])


# 
num = int(input())
results = []

def find_computer(a, b):
    if a == 0:
        return 10
    
    patterns = {
        1: [1],
        2: [2, 4, 8, 6],
        3: [3, 9, 7, 1],
        4: [4, 6, 4, 6],
        5: [5],
        6: [6],
        7: [7, 9, 3, 1],
        8: [8, 4, 2, 6],
        9: [9, 1, 9, 1],
        0: [10]
    }

    pattern = patterns[a % 10]
    # print("dddd ===> ", pattern) # 만약 a%10이 2이면, [2, 4, 8, 6]이 출력된다.
    # print("==> ", pattern[(b-1) % len(pattern)]) # index는 0부터 시작하므로 b-1을 해준다.
    # print("len = ", len(pattern)) # len(pattern) 은 a 값에 몇 개 있는지. 예를 들어, 2이면 4가, 5이면 1이 나온다.

    return pattern[(b-1) % len(pattern)]

for _ in range(num):
    a, b = map(int, input().split())
    results.append(find_computer(a, b))

for i in results:
    print(i)
