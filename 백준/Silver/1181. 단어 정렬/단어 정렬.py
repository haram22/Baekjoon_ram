import sys
N = int(sys.stdin.readline())
input_list = []
final_list = []

for _ in range(N) :
    user_input = sys.stdin.readline().rstrip('\n')
    input_list.append(user_input)
final_list = list(set(input_list))
result = sorted(final_list, key=lambda x : (len(x), x)  )

for word in result :
    print(word)