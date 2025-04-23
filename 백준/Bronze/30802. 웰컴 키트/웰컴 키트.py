N = int(input())
size_input = list(map(int, input().split()))
t, p = map(int, input().split())
t_num = 0
for i in range(len(size_input)) :
    if size_input[i] % t == 0 :
        t_num += size_input[i] / t
    else :
        t_num += (size_input[i] // t) + 1
print(int(t_num))
print(N // p, N % p)